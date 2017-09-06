# Logout function
-------

## Example:

    """
    This way, the logout functionality will revoke the complete session:
    """
  
    from django.contrib.auth import logout

    def logout_view(request):
        
        # Logging logout
        log.info('Logout Successful : {user} via ip: {ip}'.format(
            user=user,
            ip=ip
        ))

        logout(request)
        
        # Redirect to a success page.
        return redirect('login')

    """
    Django has inbuilt logout functionality
    """

    # Adding urls.py 

    from django.conf.urls import url
    from django.conf import settings
    from django.contrib.auth.views import logout

    urlpatterns = [
        url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
    ]

    # Add URI in Settings.py

    LOGOUT_REDIRECT_URL = '/login'
