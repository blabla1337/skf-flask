# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/loggedin", methods=['GET'])
def loggedin():
    username = request.args.get('username')
    sessionid=request.cookies.get('sessionid')
    hash = hashlib.sha256(username.encode('utf-8')).hexdigest()
    if(sessionid is hash):
        msg="Wellcome " + username
        return render_template("loggedin.html",username=username,msg=msg)
    else:
        txt='You have to login first'   
        return render_template("index.html",msg=txt)

@app.route("/logout", methods=['GET'])
def logout():
    txt=''
    if request.method == "GET":
        txt='You successfully logged out'
        res = make_response(render_template('index.html',msg=txt))
        res.set_cookie('sessionid', '', expires=0)
        return res
    txt="You are not logged out"
    return render_template('index.html',msg=txt)
```
 
-----SPLIT-----
 
# Answer

It is a Gain Privileges issue. The client session depends on 'sessionid' value and it can be easily generated for any users. The code shows, 'sha256(user)' generates secret key and the attacker can do the same calculation for any users.
