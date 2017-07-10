var tap = require('tap');
var exec = require('child_process').exec;

tap.test('Should point to cli.bithound.io settings page', function (t) {
  exec('node bithound token', function (err, stdout, stderr) {
    tap.notOk(err);
    tap.equal(stdout, 'https://bithound.io/settings/github/bithound/cli.bithound.io/integrations\n');
    t.end();
  });
});

