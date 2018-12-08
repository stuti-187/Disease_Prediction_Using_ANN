$(document).ready(function(){
  $(window).on('scroll',function() {
    var scrolltop = $(this).scrollTop();

    if(scrolltop >= 215) {
      $('.fixedbar').fadeIn(250);
    }

    else if(scrolltop <= 210) {
      $('.fixedbar').fadeOut(250);
    }
  });
});/**
 * Created by STUTI on 30-09-2016.
 */
/**
 * Created by STUTI on 03-10-2016.
 */
