import random
from django.http import response
from django.http.response import JsonResponse
import pyotp
import base64
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from .models import Profile,Address,Card
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from Orders.models import Order

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')
def login_view(request):
    if(request.method == 'POST'):
        email_or_phone = request.POST.get('email_or_phone')
        password = request.POST.get('password')
        profile_by_phone = Profile.objects.filter(phone=email_or_phone).first()
        user_by_email = User.objects.filter(email= email_or_phone).first()
        if((user_by_email == None) and (profile_by_phone==None)):
            messages.warning(request, f'No such User')
        if(profile_by_phone):
            user=authenticate(username=profile_by_phone.user.username,password=password)
            if(user):
                login(request,user)
            else:
                messages.warning(request, f'Wrong Password')
        if(user_by_email):
            user=authenticate(username=user_by_email.username,password=password)
            if(user):
                login(request,user)
            else:
                messages.warning(request, f'Wrong Password')
    if(request.user.is_authenticated):
        return redirect('home')
        # print(email_or_phone,password)
    return render(request,'Accounts/login.html',{'title':'Login'})
def signup_view(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        username=request.POST.get('username')
        password=request.POST.get('password')
        if(len(User.objects.filter(username=username))==0):
            if(len(User.objects.filter(email=email))==0):
                if(len(Profile.objects.filter(phone=phoneno))==0):
                    new_user = User.objects.create_user(username,email,password)
                    profile = Profile(user=new_user,phone=phoneno)
                    profile.save()
                    login(request,new_user)
                else:
                    messages.warning(request, f'Phone No already in use')
            else:
                messages.warning(request, f'Email id already in use')

        else:
            messages.warning(request, f'Username already in use')
    if(request.user.is_authenticated):
        return redirect('home')
    return render(request,'Accounts/signup.html',{'title':'Signup'})
def forgot(request):
    if request.method == "POST":
        email_or_phone = request.POST.get('email_or_phone')
        key2 = random.randint(1, 999999)
        request.session['key2'] = key2
        profile_by_phone = Profile.objects.filter(phone=email_or_phone).first()
        user_by_email = User.objects.filter(email= email_or_phone).first()
        if((user_by_email == None) and (profile_by_phone==None)):
            messages.warning(request, f'No such User')
        if(profile_by_phone):
            request.session['phone'] = email_or_phone
            request.session['email'] = profile_by_phone.user.email
            return redirect('verify')
        if(user_by_email):
            request.session['phone'] = Profile.objects.filter(user=user_by_email).first().phone
            request.session['email'] = email_or_phone
            return redirect('verify')
    return render(request,'Accounts/forgot.html',{'title':'Forgot Password'})

def verify(request):
    phone = request.session['phone']
    key1 = base64.b32encode(bytes(phone, 'utf-8'))
    totp = pyotp.HOTP(key1)
    key2 = request.session['key2']
    send_mail('password reset', 'Shoe Shop website password reset otp='+str(totp.at(key2)),
              settings.EMAIL_HOST_USER, [request.session['email']], fail_silently=False)
    print(totp.at(key2))
    if request.method == "POST":
        otp = request.POST['otp']
        if(totp.verify(otp, key2)):
            request.session['otp'] = otp
            return redirect('reset')
        else:
            messages.warning(request, f'Invalid OTP')
            return redirect('verify')
    return render(request, 'Accounts/verify.html', {'title': 'Verify OTP'})

def reset(request):
    
    if(request.method == 'POST'):
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password2 == password1):
            try:
                validate_password(password1)
            except ValidationError as e:
                message = list(e)
                messages.warning(request, message[0])
            else:
                phone = request.session['phone']
                email = request.session['email']
                key1 = base64.b32encode(bytes(phone, 'utf-8'))
                totp = pyotp.HOTP(key1)
                key2 = request.session['key2']
                otp = request.session['otp']
                if(totp.verify(otp, key2)):
                    user = User.objects.filter(email=email).first()
                    print(user)
                    user.set_password(password1)
                    user.save()
                    messages.success(request, f'Succesfully changed password')
                    return redirect('login')
                else:
                    messages.warning(request, f'Passwords dont match')
                    return redirect('reset')
        else:
            messages.warning(request,f'Passwords dont match')
    return render(request, 'Accounts/reset.html', {'title': 'Reset Password'})
@login_required
def profile(request):
    if(request.method=='POST'):
        if(request.POST.get('email')):
            email = request.POST.get('email')
            if(len(User.objects.filter(email=email))==0):
                request.user.email=email
                request.user.save()
                return JsonResponse({'response':'Email Address Changed Succesfully','tag':'success'})
            else:
                return JsonResponse({'response':'Email Already In Use','tag':'warning'})
        if(request.POST.get('phone')):
            phone = request.POST.get('phone')
            if(len(Profile.objects.filter(phone=phone))==0):
                user_profile=Profile.objects.filter(user=request.user).first()
                user_profile.phone=phone
                user_profile.save()
                return JsonResponse({'response':'Phone Number Changed Succesfully','tag':'success'})
            else:
                return JsonResponse({'response':'Phone Number Already In Use','tag':'warning'})
        if(request.POST.get('username')):
            username = request.POST.get('username')
            if(len(User.objects.filter(username=username))==0):
                request.user.username=username
                request.user.save()
                return JsonResponse({'response':'Username Changed Succesfully','tag':'success'})
            else:
                return JsonResponse({'response':'Username Already In Use','tag':'warning'})
    phone = Profile.objects.filter(user=request.user).first().phone
    return render(request,'Accounts/profile.html',{'phone':phone,'title':request.user.username})
@login_required
def address(request):
    if(request.method=='POST'):
        print(request.POST)
        if(request.POST.get('address')):
            post_addr=Address(
                user=request.user,
                name=request.POST.get('name'),
                phone = request.POST.get('phone'),
                pincode = int(request.POST.get('pincode')),
                address = request.POST.get('address'),
                city = request.POST.get('city'),
                state = request.POST.get('state'),
                landmark = request.POST.get('landmark'),
                address_type = request.POST.get('address_type')
            )
            post_addr.save()
        if(request.POST.get('delete_id')):
            delete_address = Address.objects.get(pk=request.POST.get('delete_id'))
            delete_address.delete()
            return JsonResponse({'success':True})
    user_addresses=Address.objects.filter(user=request.user)
    return render(request,'Accounts/address.html',{'title':'Manage Addresses','addresses':user_addresses})
@login_required
def address_edit(request):
    if(request.method=='POST'):
        print(request.POST)
        id=request.POST.get('id')
        if(id):
            edit_address = Address.objects.get(pk=id)
            address_dict={
                'id':id,
                'name':edit_address.name,
                'phone':edit_address.phone,
                'pincode':edit_address.pincode,
                'address':edit_address.address,
                'city':edit_address.city,
                'state':edit_address.state,
                'landmark':edit_address.landmark,
                'address_type':edit_address.address_type
            }
            return JsonResponse(address_dict)
        save_id=request.POST.get('save_id')
        if(save_id):
            save_address = Address.objects.get(id=save_id)
            print(save_address)
            save_address.name=request.POST.get('name')
            save_address.phone=request.POST.get('phone')
            save_address.pincode=request.POST.get('pincode')
            save_address.address=request.POST.get('address')
            save_address.city=request.POST.get('city')
            save_address.state=request.POST.get('state')
            save_address.landmark=request.POST.get('landmark')
            save_address.address_type=request.POST.get('address_type')
            save_address.save()
            return JsonResponse({'success':True})
@login_required
def cards(request):
    if(request.method=='POST'):
        print(request.POST)
        name_on_card=request.POST.get('name_on_card')
        exp_date=request.POST.get('exp_date')
        card_number=request.POST.get('card_number')
        delete_id = request.POST.get('delete_id')
        if(request.POST.get('addcard')):
            new_card=Card(
                    user=request.user,
                    name_on_card=name_on_card,
                    exp_date=exp_date,
                    card_number=card_number
                    )
            new_card.save()
            new_card_dict={
                'id':new_card.id,
                "name_on_card":new_card.name_on_card,
                'exp_date':new_card.exp_date,
                'card_number':new_card.card_number
            }
            return JsonResponse(new_card_dict)
        if(delete_id):
            delete_card=Card.objects.get(pk=delete_id)
            delete_card.delete()
            return JsonResponse({'success':True})
    user_cards=Card.objects.filter(user=request.user)
    return render(request,'Accounts/cards.html',{'title':'Manage cards','cards':user_cards})

def cards_edit(request):
    if(request.method=='POST'):
        edit_id=request.POST.get('id')
        save_id=request.POST.get('save_id')
        exp_date=request.POST.get('exp_date')
        name_on_card=request.POST.get('name_on_card')
        card_number=request.POST.get('card_number')
        if(edit_id):
            edit_card=Card.objects.get(pk=edit_id)
            exp_date=edit_card.exp_date.split('/')
            print(exp_date)
            edit_card_dict={
                'id':edit_id,
                'name_on_card':edit_card.name_on_card,
                'card_number':edit_card.card_number,
                'expireMM':exp_date[0],
                'expireYY':exp_date[1]
            }
            return JsonResponse(edit_card_dict)
        if(save_id):
            save_card=Card.objects.get(pk=save_id)
            save_card.name_on_card=name_on_card
            save_card.card_number=card_number
            save_card.exp_date=exp_date
            save_card.save()
            return JsonResponse({'success':True})
        return JsonResponse({'success':True})


def myorders(request):
    orders=Order.objects.filter(user_id=request.user)
    for i in orders:
        print('..........')
        for j in i.cart_ids.all():
            print(j)
    return render(request,'Accounts/myorders.html',{'orders':orders})