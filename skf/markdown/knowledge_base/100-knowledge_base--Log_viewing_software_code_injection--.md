# Code injection log viewing software
-------

## Description:

Whenever user supplied input is being handled into log viewing software, this sofware
can be manipulated by potential attackers whenever this input is not properly being sanitized
before outputting in the software. Depending on the context of where the supplied input is being used
the could lead to an entire subset of attacks.

## Solution:

You should consider these three controls when supplying information to the log viewing software:

- Design: If at all possible, avoid logging data that came from external inputs.

- Implementation: Ensure that all log entries are statically created, or if they must
 record external data that the input is vigorously white-list checked.

- Run time: Avoid viewing logs with tools that may interpret control characters in the
 file, such as command-line shells.

Also verify that all non-printable symbols and field separators are properly encoded in log entries,
to prevent log injection.
