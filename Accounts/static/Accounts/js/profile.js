function toggleusername(){
    flag = document.getElementById("username").disabled
    document.getElementById("username").disabled=!flag
    if(flag){
      document.getElementById('changeusernamebutton').style.visibility='visible'
    }
    else{
      document.getElementById('changeusernamebutton').style.visibility='hidden'
    }
  }
  function toggleemail(){
    flag = document.getElementById("email").disabled
    document.getElementById("email").disabled=!flag
    if(flag){
      document.getElementById('changeemailbutton').style.visibility='visible'
    }
    else{
      document.getElementById('changeemailbutton').style.visibility='hidden'
    }
  }
  function togglephone(){
    flag = document.getElementById("phone").disabled
    document.getElementById("phone").disabled=!flag
    if(flag){
      document.getElementById('changephonebutton').style.visibility='visible'
    }
    else{
      document.getElementById('changephonebutton').style.visibility='hidden'
    }
  }
  function changeusername(){
    username = document.getElementById('username').value
    $.ajax({
      url:url,
      method:'post',
      data:{'username':username,'csrfmiddlewaretoken':csrf_token},
      success:function(res){
        console.log(res);
        document.getElementById('messagediv').innerHTML='<div class="alert alert-'+res.tag+'">'+res.response+'</div>'
      }
    })
  }
  function changeemail(){
    email = document.getElementById('email').value
    console.log(email)
    $.ajax({
      url:url,
      method:'post',
      data:{'email':email,'csrfmiddlewaretoken':csrf_token},
      success:function(res){
        console.log(res);
        document.getElementById('messagediv').innerHTML='<div class="alert alert-'+res.tag+'">'+res.response+'</div>'
      }
    })
  }
  function changephone(){
    phone = document.getElementById('phone').value
    console.log(phone)
    $.ajax({
      url:url,
      method:'post',
      data:{'phone':phone,'csrfmiddlewaretoken':csrf_token},
      success:function(res){
        console.log(res);
        document.getElementById('messagediv').innerHTML='<div class="alert alert-'+res.tag+'">'+res.response+'</div>'
      }
    })
  }
