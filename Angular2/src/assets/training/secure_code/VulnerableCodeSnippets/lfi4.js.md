# Question
 
What is the problem here?
 
```
const express = require('express')
const app = express()
const port = 1337

app.get('/download', (req, res) => {
  const file = downloadFile(req.query.fileName).toString()
  res.send(file)
})

function downloadFile(filePath){
  result = fs.readFileSync(filePath)
  return result;
}
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'fileName' parameter is not sanitized for OS file injections. End-users can download any files they want with the service account privilege.
