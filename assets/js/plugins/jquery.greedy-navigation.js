$(document).ready(function() {
  var $nav = $('.greedy-nav');
  var $btn = $('.greedy-nav__toggle');
  var $visibleLinks = $('.visible-links');
  var $hiddenLinks = $('.hidden-links');
  
  // Logic for greedy navigation
  var availableSpace = function() {
    return $nav.width() - $visibleLinks.width() - 80;
  };
  
  var checkWidth = function() {
    var $navClone = $visibleLinks.clone();
    $navClone.removeClass('visible-links');
    var navWidth = $nav.width();
    var totalWidth = 0;
    
    $navClone.each(function(index) {
      totalWidth += $(this).width();
      if (totalWidth > navWidth - 80) {
        $(this).addClass('greedy-nav__hidden');
        $hiddenLinks.append($(this).clone());
      } else {
        $(this).removeClass('greedy-nav__hidden');
      }
    });
  };
  
  checkWidth();
  $(window).resize(checkWidth);
  
  $btn.on('click', function(e) {
    e.preventDefault();
    $hiddenLinks.toggleClass('hidden');
    $btn.toggleClass('is-active');
  });
});
