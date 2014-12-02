window.onload = displayTotalPrice;

function displayTotalPrice()
{
  var product_number = document.getElementById("product_number").value;
  var product_price = parseFloat(document.getElementById("product_price").innerHTML);
  document.getElementById('PRODUCT_TOTAL_PRICE').innerHTML = product_price * product_number;
}

function changeNumber(a) {
  var product_number = document.getElementById("product_number");
  var p = parseInt(product_number.value);
  if (a == 1) {
    if (p < 1000) product_number.value = ++p;
  }
  else {
    if (p > 1) product_number.value = --p;
  }
}

function addToCart(productID)
{
  product_id = productID;
  quantity = 1;
  if (document.getElementById("product_number"))
    {
      quantity = document.getElementById("product_number").value;
    }
  Ajax.call('/cart/add/', 'product_id='+ product_id +'&quantity=' + quantity, addToCartResponse, 'POST', 'TEXT');
}

function jumpToCart(){
  location.href = "/cart/show/";
}

function addToCartResponse(result)
{
  $("#buy_lay").show();
  $("#buy_lay_frm").show();
  $("#buy_lay_frm").css({"top":($(window).height()/2-70)+'px'});
}

$(function() {
  $("#btn_continue").click(function(){
    $("#buy_lay").hide();
    $("#buy_lay_frm").hide();
});
  $("#btn_check").click(function(){
    window.location='/cart/show/';
  });
  $(document).bind("click",function(){
    $("#buy_lay").hide();
    $("#buy_lay_frm").hide();
  });
});