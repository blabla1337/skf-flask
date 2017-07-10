# git-origin-url

[![Build Status](http://img.shields.io/travis/wilmoore/node-git-origin-url.svg)](https://travis-ci.org/wilmoore/node-git-origin-url) [![NPM version](http://img.shields.io/npm/v/git-origin-url.svg)](https://www.npmjs.org/package/git-origin-url) [![NPM downloads](http://img.shields.io/npm/dm/git-origin-url.svg)](https://www.npmjs.org/package/git-origin-url) [![LICENSE](http://img.shields.io/npm/l/git-origin-url.svg)](license)

> Retrieve the git remote origin URL of the current repo for [Node.js][].

## Example

    var origin = require('git-origin-url');

    origin(function (err, url) {
      if (err) throw err;
      console.log(url);
    });

    //=> https://github.com/wilmoore/node-git-origin-url.git

## Installation

    $ npm install git-origin-url

## Inspiration

- [resolve-git-remote][]

## License

  [MIT](license)

[resolve-git-remote]:   https://github.com/thlorenz/resolve-git-remote
[Node.js]:              http://nodejs.org
