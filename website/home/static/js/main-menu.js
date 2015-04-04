$(function(){
    $( 'li.has-submenu' ).on( 'click.menu', function( e ){
        e.stopPropagation();
        $( this ).children( '.mainmenu-submenu' ).slideToggle();
    });
});