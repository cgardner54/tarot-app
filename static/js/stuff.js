AJAX:
$(document).ready(function(){
  $(".card1").click(function(){
    $(".card1").toggleClass("is-flipped");
  });
    });
$(document).ready(function(){
  $(".card2").click(function(){
    $(".card2" ).toggleClass("is-flipped");
  });
    });
$(document).ready(function(){
  $(".card3").click(function(){
    $(".card3" ).toggleClass("is-flipped");
  });
    });

    
// var card = document.querySelector('.card');
// card.addEventListener( 'click', function() {
//   card.classList.toggle('is-flipped');
// });
// document.getElementById("flip-card-inner").addEventListener("click", function() {
//   document.getElementById("flip-card-back", "flip-card-front", "flip-card-inner").classList("flippy")
//     });


// onclick handler, target the cards:
// onclick reveal cards
// onhover of card image reveal meaning, upright or reversed


// object.addEventListener("click", myScript);

// object.onclick = function(){myScript};

// <element onclick="myScript">
// function(){
//   $("#card3").fadeIn("slow")
//   console.log($("#card3").val())