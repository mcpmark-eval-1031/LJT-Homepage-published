$(document).ready(function(){
  $('.container .header').click(function(){
    $(this).next('.content').slideToggle();
  });
});
