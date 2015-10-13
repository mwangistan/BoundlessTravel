function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$(function(){
	$('button').click(function(e){
		e.preventDefault();
		var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		var name = $('#name').val();
		var email = $('#email').val();
		var message = $('#message').val();
		var subject = $('#subject').val();
		
		if (subject == ""){
			$('#1').addClass('has-error');
		}
		else{
			$('#1').removeClass('has-error');
		}
		
		if (name == ""){
			$('#2').addClass('has-error');
		}
		
		else{
			$('#2').removeClass('has-error');
		}
		
		if (email == "" || re.test(email) == false) {
			$('#3').addClass('has-error');
		}
		
		else{
			$('#3').removeClass('has-error');
		}
		
		if (message == ""){
			$('#4').addClass('has-error');
		}
		
		else{
			$('#4').removeClass('has-error');
		}
		
		if (name != "" && (email != "" && re.test(email) == true) && message != "" && subject !== ""){
			create_post();
		}
		
	});
	function create_post(){
	$.ajax({
			url: "/",
			type: "POST",
			data: {subject: $('#subject').val(), name: $('#name').val(), email: $('#email').val(), message: $('#message').val()
				  },
			
			success: function(json){
				$('#name').val('');
				$('#email').val('');
				$('#message').val('');
				$('#subject').val('');
				
				alert(json);
			},
			
			error: function(xhr, errmsg, err){
	
				$('#result').html("<div class='alert'>Oops We have encountered an error: " +errmsg + "<a href='#' class='close'>&times;</a></div>");
			}
		});
	};
});
