function rendernav(){
    $.ajax({
        url:nav_url,
        type:'get',
        success:function(res){
          seafood = document.getElementById('navbar-seafood')
          meat=document.getElementById('navbar-meat')
          seafood_innerHTML=''
          for (var i in res.seafood_dict){
            seafood_innerHTML=seafood_innerHTML+'<a href='+category_url+res.seafood_dict[i]+'>'+i+'</a>'
          }
          seafood.innerHTML=seafood_innerHTML
          meat_innerHTML=''
          for (var i in res.meat_dict){
            meat_innerHTML=meat_innerHTML+'<a href='+category_url+res.meat_dict[i]+'>'+i+'</a>'
          }
          meat.innerHTML=meat_innerHTML
        }
      })
}