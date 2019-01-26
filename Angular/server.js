//Install express server
const express = require('express');
const path = require('path');
const app = express();

// Serve only the static files form the dist directory
app.use(express.static(__dirname + '/dist/skf-flask/Angular'));

app.get('/*', function(req,res) {
	res.sendFile(path.join(__dirname+'/dist/skf-flask/Angular/index.html'));
});

const PORT = 8080;
const HOST = '0.0.0.0';

app.listen(PORT, HOST, function () {
  console.log('Server listening : ' + PORT);
});
