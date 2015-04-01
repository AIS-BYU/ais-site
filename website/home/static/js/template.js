$(function(){
    
	//Homepage Slider
    var options = {
        nextButton: false,
        prevButton: false,
        pagination: true,
        animateStartingFrameIn: true,
        autoPlay: true,
        autoPlayDelay: 5000,
        preloader: true
    };
    // Initalize homepage slider
    $("#sequence").sequence(options).data("sequence");

	//Make Videos Responsive
	$(".video-wrapper").fitVids();

	//Initialize tooltips
	$('.show-tooltip').tooltip();

	$( window ).resize(function() {
		$('.col-footer:eq(0), .col-footer:eq(1)')
            .css('height', '')
            .css('height', (Math.max($('.col-footer:eq(0)').height(), $('.col-footer:eq(1)').height()) + 'px'));
	});
	$( window ).resize();

});