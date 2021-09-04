from Accounts.views import address, cards
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import Cart,Product,Order
from Accounts.models import Address,Card
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def cart(request):
    cart_items=Cart.objects.filter(user_id=request.user).filter(ordered=False)
    no_items=False
    if(len(cart_items)==0):
        no_items=True
    grand_total=0
    for i in cart_items:
        grand_total=grand_total+i.total_price
    delete_id=request.POST.get('delete_id')
    edit_id=request.POST.get('edit_id')
    quantity=request.POST.get('quantity')
    if(delete_id):
        delete_cart=Cart.objects.get(pk=delete_id)
        delete_cart.delete()
        cart_items=Cart.objects.filter(user_id=request.user).filter(ordered=False)
        grand_total=0
        for i in cart_items:
            grand_total=grand_total+i.total_price
        return JsonResponse({'delete_id':delete_id,'grand_total':grand_total,'grand_total':grand_total})
    if(edit_id and quantity):
        edit_cart=Cart.objects.get(pk=edit_id)
        edit_cart.quantity=int(quantity)
        edit_cart.save()
        cart_items=Cart.objects.filter(user_id=request.user).filter(ordered=False)
        grand_total=0
        for i in cart_items:
            grand_total=grand_total+i.total_price
        return JsonResponse({'edit_id':edit_id,'price':edit_cart.total_price,'grand_total':grand_total})
    user_addresses=Address.objects.filter(user=request.user)
    user_cards=Card.objects.filter(user=request.user)
    return render(request,'Orders/cart.html',{'no_items':no_items,'cart_items':cart_items,'grand_total':grand_total,'cards':user_cards,'addresses':user_addresses})

def addtocart(request):
    if(request.method=='POST'):
        if(request.user.is_authenticated):
            product_id=request.POST.get('product_id')
            if(product_id):
                the_product =Product.objects.get(pk=product_id)
                product_cart=Cart.objects.filter(product_id=the_product)
                if(len(product_cart.filter(ordered=False))==0):
                    new_cart=Cart(
                        product_id=the_product,
                        user_id=request.user
                    )
                    new_cart.save()
                    return JsonResponse({'status':'Product added to cart'})  
                else:
                    old_cart=product_cart.filter(ordered=False).first()
                    old_cart.quantity=old_cart.quantity+1
                    old_cart.save()
                    return JsonResponse({'status':'Product already in cart,quantity added'})    
        else:
            print(request.POST)
            return JsonResponse({'status':'Login First'})                  
    return JsonResponse({'sucess':True})

def checkout(request):
    if(request.method=='POST'):
        address_id=request.POST.get('address_id')
        card_id=request.POST.get('card_id')
        selected_card_id=request.POST.get('selected_card_id')
        selected_address_id=request.POST.get('selected_address_id')
        if(address_id):
            address = Address.objects.get(pk=address_id)
            address_dict={
                'id':address.id,
                'name':address.name,
                'phone':address.phone,
                'pincode' :address.pincode,
                'address' : address.address,
                'city' : address.city,
                'state' : address.state,
                'landmark' : address.landmark,
                'address_type':address.address_type
            }
            return JsonResponse(address_dict)
        if(card_id):
            card=Card.objects.get(pk=card_id)
            card_dict={
                'id':card.id,
                'name_on_card':card.name_on_card,
                'card_number':card.card_number
            }
            return JsonResponse(card_dict)
        if(selected_address_id and selected_address_id):
            cart=Cart.objects.filter(user_id=request.user,ordered=False)
            total=0
            for i in cart:
                total = total+i.total_price
            print(total)
            order=Order(
                user_id=request.user,
                address_id = Address.objects.get(pk=selected_address_id),
                delivery_status = "Yet to be dispatched",
                total_price=total
            )
            order.save()
            order.cart_ids.set(cart)
            print(order)
            for i in cart:
                i.ordered = True
                i.save()
            return JsonResponse({'status':'added'})
    return JsonResponse({'success':True})

def confirmation(request):
    return render(request,'Orders/confirmation.html')