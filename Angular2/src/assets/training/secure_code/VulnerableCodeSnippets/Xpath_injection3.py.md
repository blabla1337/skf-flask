# Question
 
What is the problem here?
 
```
...
tree = ET.parse('books.xml')
root = tree.getroot()

@app.route('/books')
def books():
    bookName = request.args['bookName']
    query = "./books/book/[@bookname='" + bookName + "']/writer"
    elmts = root.findall(query)
    return 'Writer %s' % list(elmts)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')
```
 
-----SPLIT-----
 
# Answer

It is an XPath injection issue. 'bookName' parameter is not being sanitized and the attacker can inject malicious commands to the query.
