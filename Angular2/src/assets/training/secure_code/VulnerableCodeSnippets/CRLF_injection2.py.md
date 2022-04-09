# Question
 
What is the problem here?
 
```
...
@app.route('/')
def index():
    return 'Home page'

@app.route('/Jobs', methods=['GET'])
def userJob():
    job = request.args.get('preferredJob', 'any')
    if isValid(job):
        setHeaderCookie(job)

def isValid(job):
    #check if it exists in our db
    if exists:
        ...
        return True
    else:
        ...
        return False

def setHeaderCookie(job):
    #set header cookie to show custumer based advertisements
    resp = make_response(render_template('side_advertisements.html'))
    resp.set_cookie('PreferredJob', job)
    return resp
```
 
-----SPLIT-----
 
# Answer

It is an CRLF injection issue. 'preferredJob' is not being sanitized properly before processing. If the attacker provides 'CR' or 'LF' characters to the parameter, she/he can manipulate the service responses. For example: 'Name1\r\nContent-Length:40\r\n\r\n'