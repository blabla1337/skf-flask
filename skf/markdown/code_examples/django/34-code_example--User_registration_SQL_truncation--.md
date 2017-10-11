# User registration / Sql truncation prevention
-------

## Example:

    """
    In order to prevent Column truncation sql injection Solution we have to make sure the
    applications structural logic does not mismatches with the database structural logic.
    To achieve this imagine the follow example of a database structure of a users table

    TABLE users
    ------------------------------------------------------------
    |	     *Name*          |	   *Type*       |    *Extra*     |
    ------------------------------------------------------------
    |        ID	           |    Int(11)       | AUTO_INCREMENT |
    ------------------------------------------------------------
    |       Username  	   |    char(21)      |                |
    ------------------------------------------------------------
    |       Password       |  Varchar(255)    |                |
    ------------------------------------------------------------
    |      last_login      |      date        |                |
    ------------------------------------------------------------   
    |      is_superuser    |      int(1)      |                |
    ------------------------------------------------------------
    |      first_name      |    varchar(30)   |                |
    ------------------------------------------------------------
    |      last_name       |    varchar(30)   |                |
    ------------------------------------------------------------
    |      email           |    varchar(30)   |                |
    ------------------------------------------------------------
    |      is_staff        |      int(1)      |                |
    ------------------------------------------------------------
    |      is_active       |      int(1)      |                |
    ------------------------------------------------------------
    |      date_joined     |      date        |                |
    ------------------------------------------------------------
    """

    //For URL routes for User Registration

    from django.conf.urls import url
    from mysite.core import views as core_views

    urlpatterns = [
        ...
        url(r'^signup/$', core_views.signup, name='signup'),
    ]

    //View for signup
    from django.contrib.auth import login, authenticate
    from django.shortcuts import render, redirect

    from .forms import SignUpForm

    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = SignUpForm()
        return render(request, 'polls/signup.html', {'form': form})

    //Template for signup.html
    {% block content %}
      <h2>Sign up</h2>
      <form method="post">
        {% csrf_token %}
        {% for field in form %}
          <p>
            {{ field.label_tag }}<br>
            {{ field }}
            {% if field.help_text %}
              <small style="color: grey">{{ field.help_text }}</small>
            {% endif %}
            {% for error in field.errors %}
              <p style="color: red">{{ error }}</p>
            {% endfor %}
          </p>
        {% endfor %}
        <button type="submit">Sign up</button>
      </form>
    {% endblock %}

    //forms.py for extra fields
    class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )            