# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/viewaddress", methods=['POST', 'GET'])
def showaddress():
    if not session.get('usersessionid'):
        return render_template('403.html')
        
    sqli  = Classes()
    address = sqli.getAdd(session.get('userId'))
    return render_template("viewaddress.html", address = address)

@app.route("/user")
def user():
    ldap_connection = ldap.initialize("ldap://127.0.0.1:389")
    distinguished_name =  request.args['dn']
    username =  request.args['username']
    search_filter = "(&(objectClass=*)(uid=" + username + "))"
    user = ldap_connection.search_s(distinguished_name, ldap.SCOPE_SUBTREE, search_filter)
    return user[0]

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is an LDAP Injection issue. 'username' and 'dn' parameters are not being checked for any malicious LDAP chars and used in query directly. The attacker can inject LDAP chars for exploitation.
