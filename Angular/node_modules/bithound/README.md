# bitHound

[![NPM version][npm-image]][npm-url]
[![bitHound Overall Score](https://www.bithound.io/projects/badges/f907f2c0-bfbd-11e5-b2ad-73729a2991e3/score.svg)](https://www.bithound.io/github/bithound/cli.bithound.io)
[![bitHound Dependencies](https://www.bithound.io/projects/badges/f907f2c0-bfbd-11e5-b2ad-73729a2991e3/dependencies.svg)](https://www.bithound.io/github/bithound/cli.bithound.io/master/dependencies/npm)
[![bitHound Dev Dependencies](https://www.bithound.io/projects/badges/f907f2c0-bfbd-11e5-b2ad-73729a2991e3/devDependencies.svg)](https://www.bithound.io/github/bithound/cli.bithound.io/master/dependencies/npm)

## Installation:
Add the latest version of `bithound` to your package.json:

```
npm install bithound --save-dev
```

# Usage:
This script `bin/bithound` provides two cli commands:

  - `check (git url || repo token)` Checks bitHound for failing files or dependencies.
  
  - `token` Opens your browser to the repo settings page of the current project.
  
If you include `node_modules/.bin` in your `$PATH`, you can run this cli with:

```
bithound <command>
```

Otherwise, run it with: 

```
./node_modules/.bin/bithound <command>
```

# Commands

## check
Attempts to retrieve the latest status of failing criteria for a repo.

This command can be used to check the status of both public and private repos.

For public repos, use the raw git url of the repo. It will look similar to:

```
git@github.com:bithound/cli.bithound.io.git
```

For private repos, use your repo token provided by bitHound. It will look similar to:

```
8164a970-c6bb-11e5-9058-dd9db6223fa8
```

See the `token` command for how to get this value.

Run the check command as follows:

```
bithound check <git url | repo token>
```

You may optionally pass the specific branch and sha through the `--branch` and `--sha` options, respectively. However, this is 
designed to work inside a CI and, as such, the `check` command will attempt to pick up the branch and sha from the CI environment variables
when a push event is detected by the CI.

If analysis is in progress, this command will poll until analysis is complete and report the results.

Your repo token can be found on your repo settings page under _Integrations_ or by running `bithound token`. In addition, you may also configure your repo's failing criteria on that settings page.

## token

```
bithound token
```

This command takes you to your _Integrations_ section of the repo settings page for the repo that bitHound is currently found to be
a dependency of. Think of it as a shortcut to discovering your repo token.

*Please note:* This command requires git to be installed in order to properly identify the repo remote origin.

---
[npm-url]: https://npmjs.org/package/bithound
[npm-image]: https://img.shields.io/npm/v/bithound.svg

