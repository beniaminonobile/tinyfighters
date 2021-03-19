$(document).ready(function() {
    $('.loader-section-progress div').css('transition-duration', '1000ms')
    $('.loader-section-progress div').css('width', '100%')
    setTimeout(function(){
        $('.loader-section').addClass('loader-section-hide')
    }, 2000);
})