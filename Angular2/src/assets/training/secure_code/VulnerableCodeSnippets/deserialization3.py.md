# Question
 
What is the problem here?
 
```
@app.route("/")
def start():
        user = {'name': 'ZeroCool'}
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(user, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('filename.pickle', 'rb') as handle:
            a = pickle.load(handle)
        return render_template("index.html", content = a)


@app.route("/sync", methods=['POST'])
def deserialization():
        with open("pickle.hacker", "wb+") as file:
            att = request.form['data_obj']
            attack = bytes.fromhex(att)
            file.write(attack)
            file.close()
        with open('pickle.hacker', 'rb') as handle:
            a = pickle.load(handle)
            print(attack)
            return render_template("index.html", content = a)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. 'pickle' is an insecure deserialization library. https://github.com/blabla1337/skf-labs/blob/master/python/DES-Pickle