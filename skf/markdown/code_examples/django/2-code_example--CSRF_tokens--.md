CSRF tokens
-------

## Example:


    """
    The random CSRF token generated need to be send to the server with every form submission. 

    The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries.
    The CSRF middleware is activated by default in the MIDDLEWARE setting.
    """

    """
    In HTML Forms, for specifying the CSRF we can use the below code
    """

    <form method="post">
    	{% csrf_token %}
	</form>

	"""
    For the AJAX POST requests, ou have to remember to pass the CSRF token in as POST data with every POST request. For this reason, there is an alternative method: on each XMLHttpRequest, set a custom X-CSRFToken header to the value of the CSRF token.

    The CSRF token cookie is named csrftoken by default, but you can control the cookie name via the CSRF_COOKIE_NAME setting.

    The CSRF header name is HTTP_X_CSRFTOKEN by default, but you can customize it using the CSRF_HEADER_NAME setting.
	"""

	<script type="text/javascript">
    
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
	</script>

    """
    Using CSRF in Jinja Templates
    """
	
    <form action="" method="post">{{ csrf_input }}