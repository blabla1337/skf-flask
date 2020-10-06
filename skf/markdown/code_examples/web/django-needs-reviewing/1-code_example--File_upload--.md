# File upload
-------

## Example:

        
	"""
	In Django the file data is placed in request.FILES

	Forms should be always submitted using POST request

	It is mandatory for the HTML form to have enctype="multipart/form-data" otherwise the 
	request.FILES will be empty

	Django have proper models to handle the uploaded files : FileField and ImageField, they 
	have the reference the location where the file is  stored
	"""

	//set MEDIA_URL and MEDIA_ROOT in project's settings.py
	MEDIA_URL = '/media/'
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

	//Add the urls.py file 
	from django.conf import settings
	from django.conf.urls.static import static

	urlpatterns = [
    	//Project url patterns...
	]

	//While development you may need to serve the user uploaded files
	if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    """
   	File Upload with model Forms

    In model form approach we can store the data about the reference of the file, details such 
    description when was it uploaded. It is more convenient to perform input validation, build
    absolute path and solve the issue of file name conflict.
    """

    //Create a Model Document to store the detail
    from django.db import models

    def user_directory_path(instance, filename):
    	//file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    	return 'user_{0}/{1}'.format(instance.user.id, filename)

	class Document(models.Model):
    	description = models.CharField(max_length=255, blank=True)
    	document = models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])
    	uploaded_at = models.DateTimeField(auto_now_add=True)

    //Add validators.py for Input Validation
    import os
    from django.core.exceptions import ValidationError	

    def validate_file_extension(value):
        //[0] returns path+filename
    	ext = os.path.splitext(value.name)[1]  
    	
        //Adding valid extensions
        valid_extensions = ['.jpg', '.png']
    	
        if not ext.lower() in valid_extensions:
            //Adding logging for extension error
            log.error('Wrong Extension Uploaded: {user} via ip: {ip}'.format(
                user=user,
                ip=ip
            ))

        	raise ValidationError(u'Unsupported file extension.')

    //Create a forms.py which will process the forms
    from django import forms
	from .models import Document

	class DocumentForm(forms.ModelForm):
    	class Meta:
        	model = Document
        	fields = ('description', 'document', ) 

    //Template for upload.html 
    {% block content %}
  	<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
  	</form>

  	<p><a href="{% url 'home' %}">Return to home</a></p>
	{% endblock %}


    //Create a view for upload functionality
    
    def model_form_upload(request):
    	if request.method == 'POST':
        	form = DocumentForm(request.POST, request.FILES)
        	
            //Check whether the form is valid
            if form.is_valid():
                //Save the form data
            	form.save()

                //Upload Successful
                log.info('Uploaded Successful : {user} via ip: {ip}'.format(
                    user=user,
                    ip=ip
                ))
                return redirect('home')
    	else:
        	form = DocumentForm()
    	return render(request, 'app/upload.html', {
            'form': form
    	})