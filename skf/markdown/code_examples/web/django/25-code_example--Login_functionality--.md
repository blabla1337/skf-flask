# Login functionality
-------

## Example:


    """
    For privilege based authentication we need an extra table in your database in order to write the users privileges to.

    Django has inbuilt users table 

    TABLE users
    ---------------------------------------------------------------------------------------------------------
    |ID|password|last_login|is_superuser|first_name|last_name|email|is_staff|is_active|date_joined|username |
    ---------------------------------------------------------------------------------------------------------  
    |1 |pbkdf2_s|2017-08-31|	  0		| 	ram    |  mohan  |ra@..|   0    |    1    |2017-08-31.| ram12   |
    ---------------------------------------------------------------------------------------------------------  	
    |2 |pbkdf2_s|2017-08-29|	  0	    |	james  |  mathew |j@g..|   1    |    1    |2017-08-30.| mathew  |
    ---------------------------------------------------------------------------------------------------------  
    |3 |pbkdf2_s|2017-08-30|	  1	    |	admin  |  admin  |adm@.|   1    |    1    |2017-08-29.| admin   |
    ---------------------------------------------------------------------------------------------------------   


    Now instead of using roles in sessions we rather want to assign privileges to users
    by means of a Database-Based Authentication system.
    Now we can easily assign a user certain privileges for him to access.
    See "Privilege based authentication" code example for more information:
    
    Django authentication in default has inbuilt code for most part of the authentication
    such as login, logout, password reset
    """
    
    //Create a login Template using form in django
    //File location registration/login.html

    {% extends 'base.html' %}
    {% block title %}Login{% endblock %}
    {% block content %}
      <h2>Login</h2>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
      </form>
    {% endblock %}

    //First we need to Configure the URL routes
    //We need to import django.contrib.auth.views and add URL route for login and logout views 

    from django.conf.urls import url
    from django.contrib.auth import views as auth_views

    urlpatterns = [
        url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'} ,name='login'),
        url(r'^logout/$', auth_views.logout, name='logout'),
    ]
    
    //In settings.py, we can set the location where django will redirect after authentication
    LOGIN_REDIRECT_URL = 'home'

    """
    There is no need to write login view again, Django has inbuilt view for login.
    Proper input validation is also done in Django auth_view.login takes care for security.
    But we need to implement a proper logging system for logouts, logins, retries
    """

    //Logging is also a inbuilt feature in django, only we need to configure it
    //Add logging system in Settings.py which logs app wise

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
            },
            'applogfile': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',

                //Specify the logging file name
                
                'filename': os.path.join(DJANGO_ROOT, 'polls.log'),
                'maxBytes': 1024*1024*15, # 15MB
                'backupCount': 10,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'polls': {
                'handlers': ['applogfile',],
                'level': 'DEBUG',
            },
        },
    }

    //Add view for logging, logout, wrong logins in view.py

    import logging
    from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
    from django.dispatch import receiver

    //Create your views for logging
    log = logging.getLogger(__name__)

    @receiver(user_logged_in)
    def user_logged_in_callback(sender, request, user, **kwargs):

        //Track the IP
        ip = request.META.get('REMOTE_ADDR')

        //Logging the details 
        log.debug('login user: {user} via ip: {ip}'.format(
            user=user,
            ip=ip
        ))

    @receiver(user_logged_out)
    def user_logged_out_callback(sender, request, user, **kwargs):

        ip = request.META.get('REMOTE_ADDR')

        log.debug('logout user: {user} via ip: {ip}'.format(
            user=user,
            ip=ip
        ))

    @receiver(user_login_failed)
    def user_login_failed_callback(sender, credentials, **kwargs):

        log.warning('logout failed for: {credentials}'.format(
            credentials=credentials,
        ))