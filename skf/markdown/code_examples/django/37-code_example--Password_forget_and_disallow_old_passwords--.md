# Password forget & Disallow old passwords
-------

## Example:


    """
    Django has inbuilt feature of password reset. We just have to mentions the URL routes and
    templates.
    """

    //We need to add django.contrib.auth in INSTALLED_APPS
    INSTALLED_APPS = [
        ...
        'django.contrib.auth',
    ]

    //Add URL routes for forget password
    from django.contrib.auth import views as auth_views

    urlpatterns = [
        ...
        url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'polls/password_reset_form.html'} , name='password_reset'),
        url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'polls/password_reset_done.html'}, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, {'template_name': 'polls/password_reset_confirm.html'} , name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'polls/password_reset_complete.html'} , name='password_reset_complete'),    
    ]

    //Template for password_reset_form.html
    
    {% extends 'base.html' %}
    {% block content %}
      <h3>Forgot password</h3>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
      </form>
    {% endblock %}

    //Template for password_reset_subject.txt
    Password reset for Website
    //Template for password_reset_email.html
    {% autoescape %}
    To initiate the password reset process for your {{ user.get_username }} TestSite Account,
    click the link below:

    {{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
    If clicking the link above doesn't work, please copy and paste the URL in a new browser
    window instead.

    Sincerely,
    The TestSite Team
    {% endautoescape %}
  
    //Template for password password_reset_done.html
    {% extends 'base.html' %}
    {% block content %}
      <p>
        We've emailed you instructions for setting your password, if an account exists with the email you entered.
        You should receive them shortly.
      </p>
      <p>
        If you don't receive an email, please make sure you've entered the address you registered with,
        and check your spam folder.
      </p>
    {% endblock %}

    //Template for password_reset_confirm.html
    {% extends 'base.html' %}
    {% block content %}
      {% if validlink %}
        <h3>Change password</h3>
        <form method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <button type="submit">Change password</button>
        </form>
      {% else %}
        <p>
          The password reset link was invalid, possibly because it has already been used.
          Please request a new password reset.
        </p>
      {% endif %}
    {% endblock %}

    //Template for password_reset_complete.html
    {% extends 'base.html' %}
    {% block content %}
      <p>
        Your password has been set. You may go ahead and <a href="{% url 'signin' %}">sign in</a> now.
      </p>
    {% endblock %}

    //Setting Up SMTP Email Backend in settings.py
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'test'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'Test <noreply@example.com>'
