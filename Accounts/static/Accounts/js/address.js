function sentdeleteid(id) {
  console.log(csrf_token);
  $.ajax({
    url: url,
    method: "post",
    data: { delete_id: id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      if (res.success) {
        console.log(res);
        location.reload();
      }
    },
  });
}
function opendeletemodal(id) {
  modal.style.display = "block";
  console.log(modal_header);
  modal_body.innerHTML = "<p>Are You Sure You want to delete this address?</p>";
  modal_yes_button.onclick = function () {
    sentdeleteid(id);
  };
  modal_cancel_button.onclick = function () {
    modal.style.display = "none";
  };
}
function editaddressdata(id) {
  showform();
  $.ajax({
    url: address_edit_url,
    method: "post",
    data: { id: id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      console.log(res);
      document.getElementById("name").value = res.name;
      document.getElementById("phone").value = res.phone;
      document.getElementById("pincode").value = res.pincode;
      document.getElementById("landmark").value = res.landmark;
      document.getElementById("address").value = res.address;
      document.getElementById("city").value = res.city;
      document.getElementById("state").value = res.state;
      if (res.address_type == "home") {
        document.getElementById("home").checked = true;
      } else {
        document.getElementById("work").checked = true;
      }
      document.getElementById("editaddress").onclick = function () {
        saveaddress(id);
      };
      document.getElementById("editaddress").style.display = "block";
      document.getElementById("submitaddressbutton").style.display = "none";
    },
  });
}
function saveaddress(id) {
  if (document.getElementById("home").checked) {
    address_type = "home";
  } else {
    address_type = "work";
  }
  $.ajax({
    url: address_edit_url,
    method: "post",
    data: {
      save_id: id,
      csrfmiddlewaretoken: csrf_token,
      name: document.getElementById("name").value,
      phone: document.getElementById("phone").value,
      pincode: document.getElementById("pincode").value,
      landmark: document.getElementById("landmark").value,
      address: document.getElementById("address").value,
      city: document.getElementById("city").value,
      state: document.getElementById("state").value,
      address_type: address_type,
    },
    success: function (res) {
      if (res.success) {
        document.getElementById("address-form").reset();
        location.reload();
      }
    },
  });
}
function showaddform() {
  document.getElementById("address-form").reset();
  showform();
  document.getElementById('editaddress').style.display='none';
  document.getElementById('submitaddressbutton').style.display='block';
}
function showform() {
  document.getElementById("address-form").style.display = "block";
  document.getElementById("addresses-section").style.display = "none";
}
function submitnewaddress() {
  document.getElementById("address-form").submit();
  document.getElementById("address-form").reset();
}
function canceladdress() {
  document.getElementById("address-form").reset();
  document.getElementById("address-form").style.display = "none";
  document.getElementById("addresses-section").style.display = "block";
}
var modal = document.getElementById("myModal");
var modal_body = document.getElementById("modal-body");
var modal_header = document.getElementById("modal-header");
var modal_yes_button = document.getElementById("modal-yes-button");
var modal_cancel_button = document.getElementById("modal-cancel-button");
