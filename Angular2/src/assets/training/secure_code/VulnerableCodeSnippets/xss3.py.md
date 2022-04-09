# Question
 
What is the problem here?
 
```
...
def get(self, request):
    return render(request, 'index.html', {})

def post(self, request):
    try:
        username = str(request.POST.get('username'))
    except:
        return HttpResponse("Invalid user " + request.POST.get('username'))

    if isValid(username):
        return redirect('/users/' + username)
    else: 
        return HttpResponse("Invalid user " + request.POST.get('username'))

def isValid (self, username):
    # control for if user name has any numbers
    if any(char.isdigit() for char in username):
        return false
    else:
        return true
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'username' parameter is vulnerable for injection attacks and no input sanitization exists. Injected javascript codes will be executed in the response.
