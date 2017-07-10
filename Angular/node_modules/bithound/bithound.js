var program = require('commander');

program
  .version(require('./package.json').version)
  .option('--repo-token [token]', 'Unique token for private repository (provided by bitHound)')
  .option('--branch [branch]', 'An optional branch argument. If not provided, the command will attempt to discover it through an env variable')
  .option('--sha [sha]', 'An optional commit sha argument. If not provided, the command will attempt to discover it through an env variable')
  .option('--timeout [minutes]', 'An optional timeout in minutes. If none is specified, 10 minutes will be used.');

program
  .command('check [url]')
  .description('Check if a sha passes bitHound analysis')
  .action(require('./commands/check'));

program
  .command('token')
  .description('Opens your browser to the repo settings page to see your token')
  .action(require('./commands/token'));

program.parse(process.argv);
