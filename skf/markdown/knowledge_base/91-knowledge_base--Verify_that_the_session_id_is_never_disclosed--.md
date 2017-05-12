# Verify that the session id is never disclosed
-------

## Description:

If the session id is disclosed in the URL the users session id can be easily obtained by
an attacker and could leak through the referrer header towards other severs. Also whenever
the session id is disclosed in the URL the possibility also arises to perform other
attacks like session fixation which could lead to session hijacking.

## Solution:

Session id should never be included in places other than the application cookie header.
