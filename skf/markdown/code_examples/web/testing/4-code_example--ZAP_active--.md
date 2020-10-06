# OWASP ZAP active
-------

## Example:

The ZAP full scan is a script that is available in the ZAP Docker images.

It runs the ZAP spider against the specified target (by default with no time limit) followed by an optional ajax spider scan and then a full active scan before reporting the results.

This means that the script does perform actual ‘attacks’ and can potentially run for a long period of time.

By default it reports all alerts as WARNings but you can specify a config file which can change any rules to FAIL or IGNORE. 

[ZAP active scan docs](https://www.zaproxy.org/docs/docker/full-scan/)
[ZAP API scan docs](https://www.zaproxy.org/docs/docker/api-scan/)