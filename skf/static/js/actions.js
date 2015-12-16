
/*---LEFT BAR ACCORDION----*/
$(function() {
    $('#nav-accordion').dcAccordion({
        eventType: 'click',
        autoClose: true,
        saveState: true,
        disableLink: true,
        speed: 'slow',
        showCount: false,
        autoExpand: true,
//        cookie: 'dcjq-accordion-1',
        classExpand: 'dcjq-current-parent'
    });
});

var Script = function () {


//    sidebar dropdown menu auto scrolling

    jQuery('#sidebar .sub-menu > a').click(function () {
        var o = ($(this).offset());
        diff = 250 - o.top;
        if(diff>0)
            $("#sidebar").scrollTo("-="+Math.abs(diff),500);
        else
            $("#sidebar").scrollTo("+="+Math.abs(diff),500);
    });

// custom scrollbar
    $("#sidebar").niceScroll({styler:"fb",cursorcolor:"#515594", cursorwidth: '3', cursorborderradius: '10px', background: '#494949', spacebarenabled:false, cursorborder: ''});

    $("html").niceScroll({styler:"fb",cursorcolor:"#515594", cursorwidth: '6', cursorborderradius: '10px', background: '#494949', spacebarenabled:false,  cursorborder: '', zindex: '1000'});

//    tool tips

    $('.tooltips').tooltip();

//    popovers

    $('.popovers').popover();
	
	// Logo animation
	
	$("a.logo").mouseover(function() { 
		$(this).find('.img').addClass('fa-spin');
	}).mouseout(function() { 
		$(this).find('.img').removeClass('fa-spin');
	});
	
	// Menu active items
	
	$('#main-content.page02').each(function () { // Create new project
		$(this).parent().find('#sidebar .page01').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .page02').addClass('act'); // Active
	});
	$('#main-content.page03').each(function () { // Create new project
		$(this).parent().find('#sidebar .page01').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .page03').addClass('act'); // Active
	});
	$('#main-content.page03a').each(function () { // Create new project
		$(this).parent().find('#sidebar .page01').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .page03a').addClass('act'); // Active
	});
	$('#main-content.page05').each(function () { // Results
		$(this).parent().find('#sidebar .page04').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .page05').addClass('act'); // Active
	});
	$('#main-content.page06').each(function () { // Results
		$(this).parent().find('#sidebar .page04').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .page06').addClass('act'); // Active
	});
	$('#main-content.page07').each(function () { // Knowledge Base
		$(this).parent().find('#sidebar .page07').addClass('act'); // Active
	});
	$('#main-content.page08').each(function () { // Code Examples
		$(this).parent().find('#sidebar .page08').addClass('act'); // Active
	});
	$('#main-content.pageB').each(function () { // Results
		$(this).parent().find('#sidebar .pageA').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .pageB').addClass('act'); // Active
	});
	$('#main-content.pageA').each(function () { // Results
		$(this).parent().find('#sidebar .pageA').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .pageC').addClass('act'); // Active
	});
	$('#main-content.pageC').each(function () { // Results
		$(this).parent().find('#sidebar .pageA').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .pageD').addClass('act'); // Active
	});	
	$('#main-content.usersAdd').each(function () { // Results
		$(this).parent().find('#sidebar .users').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .userAdd').addClass('act'); // Active
	});	
	$('#main-content.usersManage').each(function () { // Results
		$(this).parent().find('#sidebar .users').addClass('active'); // Keep sub open
		$(this).parent().find('#sidebar .userManage').addClass('act'); // Active
	});	

	
}();

$(document).ready(function() {

	$('.form-control').change(function(){
		$(this).parent().parent().toggleClass('checked', $(this).val() == 'yes');
		$(this).parent().parent().toggleClass('false', $(this).val() == 'no');
		$(this).parent().parent().toggleClass('exclude', $(this).val() == 'na');
	});

	// Page Transition
	
	$(".animsition").animsition({
		inClass               :   'fade-in',
		outClass              :   'fade-out',
		inDuration            :    1500,
		outDuration           :    800
	});	

	
	// Increase Readability
	
	$('.toggle').click(function() { 
		$(this).parent().parent().toggleClass('narrow');
		$(this).toggleClass('act');
	});
	
	// Instant Search
	
    $('input[name=search]').keyup(function () {
        var things = $("#accordion div.panel");
        var val = $(this).val();
        var regstr = val;
        var reg = new RegExp(regstr, 'i');
        things.each(function (i) {
            var match = $(this).text().match(reg) !== null;
            $(this).toggleClass('noMatch', !match);
        });
    });
	
	// Alphabetize Items
	
	var $divs = $("div.panel");
    var orderedDivs = $divs.sort(function (a, b) {
        return $(a).find("h4").text() > $(b).find("h4").text();
    });
    $("#accordion").html(orderedDivs);
	
	// Hide "Not Available Item" in Knowledge Base
	
	$("#accordion .panel a:contains('not available item')").parent().parent().parent().remove();
	
	// Select Items
	$( "#selectable" ).bind( "mousedown", function ( e ) {
		e.metaKey = true;
	} ).selectable({
		stop: function(){
			var result = $("#drop").empty();
			$(".ui-selected", this).each(function(){
				var index = $("#selectable li").index(this);
				result.append($(this).text() + '&nbsp;');
			});
		}
	});
	
});
