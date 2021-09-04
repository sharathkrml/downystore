function loadNavBar() {
  $.ajax({
    url: nav_url,
    type: "get",
    success: function (res) {
      sport_element = document.getElementById("navbar-sport");
      brand_element = document.getElementById("navbar-brand");
      category_element = document.getElementById("navbar-category");
      sport_innerHTML = "";
      for (var sport in res.Sports) {
        sport_innerHTML =
          sport_innerHTML +
          "<a href=" +
          category_url +
          res.Sports[sport] +
          ">" +
          sport +
          "</a>";
      }
      sport_element.innerHTML = sport_innerHTML;
      brand_innerHTML = "";
      for (var brand in res.Brands) {
        brand_innerHTML =
          brand_innerHTML +
          "<a href=" +
          category_url +
          res.Brands[brand] +
          ">" +
          brand +
          "</a>";
      }
      brand_element.innerHTML = brand_innerHTML;
      category_innerHTML = "";
      for (var category in res.Category) {
        category_innerHTML =
          category_innerHTML +
          "<a href=" +
          category_url +
          res.Category[category] +
          ">" +
          category +
          "</a>";
      }
      category_element.innerHTML = category_innerHTML;
    },
  });
}
function changequantity(value, id) {
  $.ajax({
    url: url,
    method: "post",
    data: {
      edit_id: id,
      quantity: value,
      csrfmiddlewaretoken: csrf_token,
    },
    success: function (res) {
      price = $("[data-id=" + res.edit_id + "]");
      price[0].innerHTML = "₹" + res.price;
      grand_total = $("[data-id=data-grand-total]");
      grand_total[0].innerHTML = "₹ " + res.grand_total;
      grand_total[1].innerHTML = "Totals &nbsp; &nbsp; ₹ " + res.grand_total;
    },
  });
}
function deletecartitem(id) {
  $.ajax({
    url: url,
    method: "post",
    data: { delete_id: id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      div = $("[data-item-id=" + res.delete_id + "]")[0];
      div.remove();
      grand_total = $("[data-id=data-grand-total]");
      grand_total = $("[data-id=data-grand-total]");
      grand_total[0].innerHTML = "₹ " + res.grand_total;
      grand_total[1].innerHTML = "Totals &nbsp; &nbsp; ₹ " + res.grand_total;
    },
  });
}

function showaddresses() {
  document.getElementById("addresses").style.display = "block";
}
function selectaddress(address_id) {
  document.getElementById("addresses").style.display = "none";
  document.getElementById("addressbutton").style.display = "block";
  $.ajax({
    url: checkout_url,
    method: "post",
    data: { address_id: address_id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      console.log(res);
      document.getElementById("selected-address").innerHTML =
        res.name + "  " + res.phone + "<br>" + res.address + " - " + res.state;
      document
        .getElementById("selected-address")
        .setAttribute("data-id", res.id);
    },
  });
}

function showcards(){
    document.getElementById("cards").style.display = "block";
}


function selectcard(card_id) {
//   console.log(card_id);
  document.getElementById("cards").style.display = "none";
  document.getElementById("cardbutton").style.display = "block";
  document.getElementById("cvv-label").style.visibility = "visible";
  $.ajax({
    url: checkout_url,
    method: "post",
    data: { card_id: card_id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      console.log(res);
      document.getElementById("selected-card").setAttribute("data-id", res.id);
      document.getElementById('selected-card-name').innerHTML='Name: '+res.name_on_card
      document.getElementById('selected-card-no').innerHTML='Card no: '+res.card_number
      document.getElementById("selected-card").style.display='block'
    },
  });
}
function openmodal(){
    document.getElementById("myModal").style.display="block"
}
function closemodal(){
    document.getElementById("myModal").style.display="none"
}
function checkout(){
    selected_address_id=document.getElementById('selected-address').getAttribute('data-id')
    selected_card_id=document.getElementById('selected-card').getAttribute('data-id')
    cvv=document.getElementById('cvv').value
    if(selected_address_id==null){
        document.getElementById('modal-body').innerHTML="Select an address"
        openmodal()
        return;
    }
    if(selected_card_id==null){
        document.getElementById('modal-body').innerHTML="Select a card"
        openmodal()
        return;
    }
    if(cvv.length!=3){
        document.getElementById('modal-body').innerHTML="Enter valid cvv"
        openmodal()
        return;
    }
    $.ajax({
        url: checkout_url,
        method: "post",
        data: { selected_card_id: selected_card_id,selected_address_id:selected_address_id, csrfmiddlewaretoken: csrf_token },
        success: function (res) {
            console.log(confirmation_url)
          console.log(res);
          window.location.href=confirmation_url
        },
      });
}

function isNumberKey(evt) {
    var charCode = (evt.which) ? evt.which : event.keyCode;
    if (charCode != 46 && charCode > 31
    && (charCode < 48 || charCode > 57))
        return false;

    return true;
}