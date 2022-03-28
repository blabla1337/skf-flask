# Question
 
What is the problem here?
 
```
@app.route("/login",methods=["POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]
      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")
      conn.commit()
      if rs:
        return redirect(url_for("home"))
      else:
        msg = "Please provide valid credentials!"
        return redirect(url_for("login"))

```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'mail' and ' passw' parameters are vulnerable for malicious injection and no input sanitization or parameterized query takes place.