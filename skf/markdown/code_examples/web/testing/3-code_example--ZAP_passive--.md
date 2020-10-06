# OWASP ZAP passive
-------

## Example:

The ZAP Baseline scan is a script that is available in the ZAP Docker images.

It runs the ZAP spider against the specified target for (by default) 1 minute and then waits for 
the passive scanning to complete before reporting the results.

This means that the script doesn't perform any actual ‘attacks’ and will run for a relatively 
short period of time (a few minutes at most).

By default it reports all alerts as WARNings but you can specify a config file which can change 
any rules to FAIL or IGNORE.

This script is intended to be ideal to run in a CI/CD environment, even against production sites.

[ZAP basline scan docs](https://www.zaproxy.org/docs/docker/baseline-scan/)
