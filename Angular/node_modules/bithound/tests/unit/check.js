var tap = require('tap');
var exec = require('child_process').exec;
var express = require('express');
var http = require('http');
var async = require('async');

var app = express();
var server = http.createServer(app);
var env = { BITHOUND_HOST: 'http://localhost:3333' };
var port = 3333;

function notFoundCommitOrRepo (err, t, server, stderr) {
  tap.equal(stderr, 'Repo or commit not found.');
  tap.equal(err.code, 1);
  server.close();
  t.end();
}

tap.test('A repo must exists', function (t) {
  server.listen(port, function () {
    app.get('/api/check/provider/owner/repo/sha', function (req, res) { return res.sendStatus(404); });

    exec('node bithound check git@github.com/provider/owner/repo.git --sha sha', { env: env }, function (err, stdout, stderr) {
      notFoundCommitOrRepo(err, t, server, stderr);
    });
  });
});

tap.test('A repo must exists', function (t) {
  server.listen(port, function () {
    app.get('/api/check/provider/owner/repo/branch/sha', function (req, res) { return res.sendStatus(404); });

    exec('node bithound check git@github.com/provider/owner/repo.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
      notFoundCommitOrRepo(err, t, server, stderr);
    });
  });
});

function equalAndClose (err, t, server) {
  tap.equal(err, null);
  server.close();
  t.end();
}

tap.test('A request can be made with a unique token', function (t) {
  server.listen(port, function (ignored) {
    var body = { complete: true, failing: false };
    app.get('/api/check/unique_token/branch/sha', function (req, res) { return res.status(200).send(body); });

    exec('node bithound check unique_token --sha sha --branch branch', { env: env }, function (err) {
      equalAndClose(err, t, server);
    });
  });
});

tap.test('A request can be made with a github git url', function (t) {
  server.listen(port, function (ignored) {
    var body = { complete: true, failing: false };
    app.get('/api/check/github/james/bond/branch/sha', function (req, res) { return res.status(200).send(body); });

    exec('node bithound check git@github.com/james/bond.git --sha sha --branch branch', { env: env }, function (err) {
      equalAndClose(err, t, server);
    });
  });
});

tap.test('A request can be made with a bitbucket git url', function (t) {
  server.listen(port, function (ignored) {
    var body = { complete: true, failing: false };
    app.get('/api/check/bitbucket/james/bond/branch/sha', function (req, res) { return res.status(200).send(body); });

    exec('node bithound check git@bitbucket.org/james/bond.git --sha sha --branch branch', { env: env }, function (err) {
      equalAndClose(err, t, server);
    });
  });
});

tap.test('Non-200 responses from bitHound should result in 1 exit code and correct stderr', function (t) {
  server.listen(port, function (ignored) {
    app.get('/api/check/github/error/400/branch/sha', function (req, res) { return res.sendStatus(400); });
    app.get('/api/check/github/error/401/branch/sha', function (req, res) { return res.sendStatus(401); });
    app.get('/api/check/github/error/403/branch/sha', function (req, res) { return res.sendStatus(403); });
    app.get('/api/check/github/error/404/branch/sha', function (req, res) { return res.sendStatus(404); });
    app.get('/api/check/github/error/500/branch/sha', function (req, res) { return res.sendStatus(500); });

    async.parallel({
      400: function (done) {
        exec('node bithound check git@github.com/error/400.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
          tap.ok(err);
          tap.equal(stderr, 'Invalid request.');
          tap.equal(err.code, 1);
          done();
        });
      },
      401: function (done) {
        exec('node bithound check git@github.com/error/401.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
          tap.ok(err);
          tap.equal(stderr, 'Authorization failed. Invalid repo token.');
          tap.equal(err.code, 1);
          done();
        });
      },
      403: function (done) {
        exec('node bithound check git@github.com/error/403.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
          tap.ok(err);
          tap.equal(stderr, 'Not permitted.');
          tap.equal(err.code, 1);
          done();
        });
      },
      404: function (done) {
        exec('node bithound check git@github.com/error/404.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
          tap.ok(err);
          tap.equal(stderr, 'Repo or commit not found.');
          tap.equal(err.code, 1);
          done();
        });
      },
      500: function (done) {
        exec('node bithound check git@github.com/error/500.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
          tap.ok(err);
          tap.equal(stderr, 'Internal server error.');
          tap.equal(err.code, 1);
          done();
        });
      }
    }, function () { server.close(); t.end(); });
  });
});

tap.test('200 responses from bitHound should result in 0 exit code', function (t) {
  var body = { complete: true, failing: false };
  server.listen(port, function (ignored) {
    app.get('/api/check/github/success/200/branch/sha', function (req, res) { return res.status(200).send(body); });

    exec('node bithound check git@github.com/success/200.git --sha sha --branch branch', { env: env }, function (err, stdout, stderr) {
      tap.notOk(err);

      server.close();
      t.end();
    });
  });
});

tap.test('Uses environment variables to discover sha and branch', function (t) {
  var body = { complete: true, failing: false };
  server.listen(port, function (ignored) {
    app.get('/api/check/github/success/200/thisisabranch/thisisasha', function (req, res) { return res.status(200).send(body); });

    function noError (done, err) {
      tap.notOk(err);
      done();
    }

    async.parallel({
      travis: function (done) {
        env.TRAVIS = true;
        env.TRAVIS_COMMIT = 'thisisasha';
        env.TRAVIS_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      jenkins: function (done) {
        env.JENKINS_URL = 'some url';
        env.GIT_COMMIT = 'thisisasha';
        env.GIT_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      circle: function (done) {
        env.CIRCLECI = true;
        env.CIRCLE_SHA1 = 'thisisasha';
        env.CIRCLE_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      codeship: function (done) {
        env.CI_NAME = 'codeship';
        env.CI_COMMIT_ID = 'thisisasha';
        env.CI_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      appveyor: function (done) {
        env.APPVEYOR = true;
        env.APPVEYOR_REPO_COMMIT = 'thisisasha';
        env.APPVEYOR_REPO_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      bitbucket: function (done) {
        env.BITBUCKET_COMMIT = 'thisisasha';
        env.BITBUCKET_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      },
      wercker: function (done) {
        env.WERCKER = true;
        env.WERKER_GIT_COMMIT = 'thisisasha';
        env.WERKER_GIT_BRANCH = 'thisisabranch';
        exec('node bithound check git@github.com/success/200.git', { env: env }, async.apply(noError, done));
      }
    }, function () { t.end(); server.close(); });
  });
});
