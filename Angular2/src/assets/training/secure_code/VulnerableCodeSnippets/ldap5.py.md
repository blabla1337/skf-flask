# Question
 
What is the problem here?
 
```
...
ldap_connection =ldap.initialize("ldap://127.0.0.1:389")
ldap_connection.simple_bind_s("cn=ldapadmin,ou=accounts,dc=com", "mysecret")

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login", methods = ['POST'])
def login():
    username = request.form['username']
    secret = request.form['secret_answer']
    if(len(secret) < 2):
	   return render_template("index.html", result = "The secret answer is at least 2 character long.")
    search_filter = "(&(cn="+username+")(sn="+secret+"))"
    try:
        result_content = ""
        result_content = ldap_connection.search_s("dc=com", ldap.SCOPE_SUBTREE, search_filter)
        print(result_content)
        if(len(result_content) > 0):
            return render_template("index.html", result = "Welcome " + username)
        else:
            return render_template("index.html", result = "Wrong identity provided.")
    except Exception as e:
        return render_template("index.html", result = "Wrong identity provided.")
```
 
-----SPLIT-----
 
# Answer

It is an LDAP Injection issue. 'username' and 'secret_answer' parameters are not being checked for any malicious injectins. The attacker can supply "admin)(!(&(1=0":"q))" combinations for login to the application. https://github.com/blabla1337/skf-labs/blob/master/python/Ldap-injection-harder
