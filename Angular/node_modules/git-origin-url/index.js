var exec = require('child_process').exec;
var trim = String.prototype.trim;

// expose `origin` function.

module.exports = origin;

/**
 * Retrieve the git remote origin URL of the current repo.
 *
 * @param {Function} fn
 * Callback to receive the result.
 */

function origin(fn) {
  'use strict';

  exec('git config --local --get remote.origin.url', function (errors, stdout, stderr) {
    var url = "";

    if (errors)  return fn(errors.stack, url);
    if (stderr)  return fn(stderr, url);

    url = trim.call(stdout);
    if (!url) return fn('Unable to find remote origin URL!', url);

    fn(null, url);
  });
};

