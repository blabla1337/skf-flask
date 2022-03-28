# Question
 
What is the problem here?
 
```
...
@app.route('/nslookup')
def nslookup():
    domainName = request.args.get("domainName")
    cmd = "nslookup " + domainName
    os.popen(cmd)
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. 'domainName' parameter is vulnerable to OS command injection attacks. An intruder can supply 'domainName' and OS command with delimeters (;,|,&, etc) to run consecutive commands.