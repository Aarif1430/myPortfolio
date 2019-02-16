
$(document).ready(function() {
  $(".blog").hide();
  $(".about").hide();

  $(window).scroll(function() {
 
    if($(window).scrollTop() > $(window).height()) {
      $('.navbar').addClass('navbar-fixed-top');
      $("body").css("margin-top", "54px");
    }
 
  });





  $(".navbar-dark ul li a[href^='#']").on('click', function(e) {

   e.preventDefault();

   var hash = this.hash;

   $('html, body').animate({
       scrollTop: $(this.hash).offset().top - $('.navbar').height() 
     }, 300, function(){

       window.location.hash = hash;
     });

});

  $(".post a").click(function(event) {
    /*
    // Prevent default anchor click behavior
    event.preventDefault();
    var url = $("#Url").attr("href");
    document.location.href = url;
    // Store hash
    var hash = this.hash;
    $('html, body').animate({
        scrollTop: $('#blog_about').offset().top
    }, 2000, function(){
 
      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;
    });*/
   document.getElementById(".base_class").innerHTML = "";

});

$(".nav li a").on('click', function(event) {
    document.getElementById("blog_about").innerHTML = "";
     switch(event.target.name){
            case 'blg':{
              $(".about").hide();
             $(".blog").show();
              break;
            }
            case 'gall':{
              $(".blog").hide();
              $(".about").show();
              break;
            }
          }
    

  // Make sure this.hash has a value before overriding default behavior
  if (this.hash !== "") {
    // Prevent default anchor click behavior
    event.preventDefault();

    // Store hash
    var hash = this.hash;

    // Using jQuery's animate() method to add smooth page scroll
    // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 3600, function(){
 
      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;
    });
  } // End if


});
 
});

// Stop carousel
$('.carousel').carousel({
  interval: false
});

function openTab(th)
            {
                window.open(th.name,'_blank');
            }