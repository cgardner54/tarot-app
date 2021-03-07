AJAX: 
$(document).ready(function(){
    $("#img").click(function(){
      $("#img").fadeOut(500)
      setInterval(
      $("#card").fadeIn(5000),
      80000)
      });
    });



// onclick handler, target the cards:
// onclick reveal cards
// onhover of card image reveal meaning, upright or reversed


// object.addEventListener("click", myScript);

// object.onclick = function(){myScript};

// <element onclick="myScript">
// function(){
//   $("#card3").fadeIn("slow")
//   console.log($("#card3").val())