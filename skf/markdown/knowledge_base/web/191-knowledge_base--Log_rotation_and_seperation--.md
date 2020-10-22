## Description:

Log separation is indispensable in order to prevent it from either radically downgrading your
application its performance or even causing a Denial of service because the server becomes
unavailable due to the flooding of logs.

## Solution:

Log rotation is an automated process used in system administration in which dated log
files are archived. Servers which run large applications, such as LAMP stacks, often
log every request: in the face of bulky logs, log rotation is a way to limit the total
size of the logs while still allowing analysis of recent events.

Log separation basically means that you have to store your log files on a different partition
as where your OS/application is running on in order to avert a Denial of service attack or the downgrading
of your application its performance.
