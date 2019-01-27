//Install express server
const express = require('express');
const path = require('path');
const app = express();

// Serve only the static files form the dist directory

console.log("Directory path--"+__dirname)

app.use(express.static(path.join(__dirname + 'dist')));

app.get('/*', function(req,res) {
	res.sendFile(path.join(__dirname+'dist/index.html'));
});

const PORT = 8080;
const HOST = '0.0.0.0';

app.listen(PORT, HOST, function () {
  console.log('Angular server listening at port : ' + PORT);
});
