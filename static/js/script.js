$(document).ready(function(){
    $('#head').click(function(){
        $(this).toggleClass('fa-times');
        $('header').toggleClass('toggle')
    });

    $(window).on('scroll load',function(){
        $('#head').removeClass('fa-items');
        $('header').removeClass('toggle')
    });
});