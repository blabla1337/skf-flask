var origin = require('git-origin-url');
var open = require('open');

module.exports = function () {
  origin(function (err, url) {
    if (err) {
      process.stderr.write('Failed to find git origin', err.message);
      return process.exit(1);
    }

    var match = url.match(/(git@(github|bitbucket).*:)(.*)(\.git)/);
    var provider = match[2];
    var fullname = match[3];

    url = ['https://bithound.io', 'settings', provider, fullname, 'integrations'].join('/');

    console.log(url);
    open(url);
    process.exit();
  });
};
