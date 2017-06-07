# Verify that the session id is never disclosed
-------

## Description:

If the session id is disclosed in the URL the users session ID can be easily obtained by
an attacker and could leak through the referrer header towards other severs. Also whenever
the session ID is disclosed in the URL the possibility also arises to perform other
attacks like session fixation which could lead to session hijacking.

## Solution:

Session ID should never be included in places other than the application cookie header.
