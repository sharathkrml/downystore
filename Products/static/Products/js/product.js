function addtocart(){
    $.ajax({
      url:addtocart_url,
      method:'post',
      data:{'product_id':product_id,'csrfmiddlewaretoken':csrf_token},
      success:function(res){
          modal.style.display = "block";
          modal_body.innerHTML="<p>"+res.status+"</p>"
          console.log(res)
          if(res.status=='Login First'){
            modal_yes_button.innerHTML="<a style='text-decoration:none;color:black;' href="+login_url+">Login</a>"
          }else{
            modal_yes_button.innerHTML="<a style='text-decoration:none;color:black;' href="+cart_url+">Proceed to cart</a>"
          }
          modal_cancel_button.onclick=function(){
                modal.style.display = "none";
          };
      }
    })
  }
  var modal = document.getElementById("myModal");
  var modal_body = document.getElementById('modal-body')
  var modal_header = document.getElementById('modal-header')
  var modal_yes_button = document.getElementById('modal-yes-button')
  var modal_cancel_button = document.getElementById('modal-cancel-button')