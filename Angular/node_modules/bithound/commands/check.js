var async = require('async');
var program = require('commander');
var request = require('request');
var git = require('git-rev-sync');

function parse (url) {
  if (!url) { return null; }

  var match = url.match(/github.com[:\/](.*)\/(.*)/) ||
    url.match(/bitbucket.org[:\/](.*)\/(.*)/);

  if (!match) { return null; }

  return {
    url: url,
    owner: match[1],
    name: match[2].replace(/\.git$/, ''),
    provider: match[0].substring(0, match[0].indexOf('.'))
  };
}

function commitInfo () {
  var branch, sha;

  if (process.env.TRAVIS) {
    if (process.env.TRAVIS_PULL_REQUEST === 'false') {
      branch = process.env.TRAVIS_BRANCH;
      sha = process.env.TRAVIS_COMMIT;
    } else {
      branch = (process.env.TRAVIS_PULL_REQUEST === 'false' ? process.env.TRAVIS_BRANCH : git.branch(process.env.TRAVIS_BUILD_DIR));
      sha = process.env.TRAVIS_COMMIT_RANGE.match(/\.\.\.(\b[0-9a-f]{5,40}\b)$/i)[1];
    }
  } else if (process.env.JENKINS_URL) {
    branch = process.env.GIT_BRANCH;
    sha = process.env.GIT_COMMIT;
  } else if (process.env.CIRCLECI) {
    branch = process.env.CIRCLE_BRANCH;
    sha = process.env.CIRCLE_SHA1;
  } else if (process.env.CI_NAME && process.env.CI_NAME === 'codeship') {
    branch = process.env.CI_BRANCH;
    sha = process.env.CI_COMMIT_ID;
  } else if (process.env.WERCKER) {
    branch = process.env.WERCKER_GIT_BRANCH;
    sha = process.env.WERCKER_GIT_COMMIT;
  } else if (process.env.APPVEYOR) {
    branch = process.env.APPVEYOR_REPO_BRANCH;
    sha = process.env.APPVEYOR_REPO_COMMIT;
  } else if (process.env.bamboo_repository_git_branch) {
    branch = process.env.bamboo_repository_git_branch;
    sha = process.env.bamboo_repository_revision_number;
  } else if (process.env.BITBUCKET_BRANCH) {
    branch = process.env.BITBUCKET_BRANCH;
    sha = process.env.BITBUCKET_COMMIT;
  } else {
    branch = git.branch(process.cwd());
    sha = git.long(process.cwd());
  }

  return {
    branch: encodeURIComponent(program.branch || branch),
    sha: program.sha || sha
  };
}

module.exports = function (url) {
  var path = (process.env.BITHOUND_HOST || 'https://bithound.io') + '/api/check/';
  var repo = parse(url);
  var commit = commitInfo();
  var stillRunning;
  var timeout = (parseInt(program.timeout, 10) || 10);

  setTimeout(function () {
    process.stderr.write('Timed out after ' + timeout + ' minute' + (timeout > 1 ? 's.' : '.'));
    return process.exit(1);
  }, timeout * 60 * 1000);

  if (!commit.branch) {
    process.stderr.write('Branch could not be determined.');
    return process.exit(1);
  }

  if (!commit.sha) {
    process.stderr.write('Commit sha could not be determined.');
    return process.exit(1);
  }

  if (!repo) path += [url, commit.branch, commit.sha].join('/'); // They provided a repo token as first arg
  else path += [repo.provider, repo.owner, repo.name, commit.branch, commit.sha].join('/');

  var requestOpts = {
    headers: {
      'Content-Type': 'application/json',
      'User-Agent': 'cli.bithound.io'
    },
    type: 'GET',
    url: path
  };
  async.doWhilst(function (done) {
    request(requestOpts, function (err, res, body) {
      var proceed = function () {
        done(err, res.statusCode, body);
      };

      if (err) return done(err);
      if (res.statusCode !== 200) {
        if (res.statusCode === 401) return done(new Error('Authorization failed. Invalid repo token.'));
        if (res.statusCode === 403) return done(new Error('Not permitted.'));
        if (res.statusCode === 404) return done(new Error('Repo or commit not found.'));
        if (res.statusCode === 400) return done(new Error('Invalid request.'));

        return done(new Error('Internal server error.'));
      }

      body = JSON.parse(body);

      stillRunning = !body.complete;

      if (body.complete) proceed();
      else setTimeout(proceed, 3000); // Poll for sha status every 3 seconds
    });
  }, function () {
    return stillRunning;
  }, function (err, status, body) {
    if (err) {
      process.stderr.write(err.message);
      return process.exit(1);
    }

    if (body.failing) process.stderr.write(body.message);

    process.exit(body.failing);
  });
};
