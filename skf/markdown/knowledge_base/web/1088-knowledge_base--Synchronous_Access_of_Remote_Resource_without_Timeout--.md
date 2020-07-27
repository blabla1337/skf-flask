##Description:

The code has a synchronous call to a remote resource, but there is no timeout for the call, or the timeout is set to infinite.

This issue can prevent the software from running reliably, since an outage for the remote resource can cause the software to hang. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

##Mitigation:
