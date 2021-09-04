function sentdeleteid(id) {
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
  modal_body.innerHTML = "<p>Are You Sure You want to delete this card?</p>";
  modal_yes_button.onclick = function () {
    sentdeleteid(id);
  };
  modal_cancel_button.onclick = function () {
    modal.style.display = "none";
  };
}

function editcarddata(id) {
  $.ajax({
    url: cards_edit_url,
    method: "post",
    data: { id: id, csrfmiddlewaretoken: csrf_token },
    success: function (res) {
      console.log(res);
      showform();
      document.getElementById("editcardbutton").style.visibility = "visible";
      document.getElementById("submitcardbutton").style.visibility = "hidden";
      document.getElementById("editcardbutton").onclick = function () {
        saveeditcarddata(res.id);
      };
      document.getElementById("expireMM").value = res.expireMM;
      document.getElementById("expireYY").value = res.expireYY;
      document.getElementById("name_on_card").value = res.name_on_card;
      document.getElementById("card_number").value = res.card_number;
    },
  });
}
function saveeditcarddata(id) {
  exp_date =
    document.getElementById("expireMM").value +
    "/" +
    document.getElementById("expireYY").value;
  $.ajax({
    url: cards_edit_url,
    method: "post",
    data: {
      save_id: id,
      csrfmiddlewaretoken: csrf_token,
      exp_date: exp_date,
      name_on_card: document.getElementById("name_on_card").value,
      card_number: document.getElementById("card_number").value,
    },
    success: function (res) {
      if (res.success) {
        document.getElementById("expireMM").value = "";
        document.getElementById("expireYY").value = "";
        document.getElementById("name_on_card").value = "";
        document.getElementById("card_number").value = "";
        location.reload();
      }
    },
  });
}
function showform() {
  document.getElementById("address-form").style.display = "block";
  document.getElementById("addresses-section").style.display = "none";
}
function showaddform() {
  document.getElementById("editcardbutton").style.visibility = "hidden";
  document.getElementById("submitcardbutton").style.visibility = "visible";
  document.getElementById("expireMM").value = "";
  document.getElementById("expireYY").value = "";
  document.getElementById("name_on_card").value = "";
  document.getElementById("card_number").value = "";
  showform();
}
function cancelcard() {
  document.getElementById("address-form").style.display = "none";
  document.getElementById("addresses-section").style.display = "block";
}
var modal = document.getElementById("myModal");
var modal_body = document.getElementById("modal-body");
var modal_header = document.getElementById("modal-header");
var modal_yes_button = document.getElementById("modal-yes-button");
var modal_cancel_button = document.getElementById("modal-cancel-button");
