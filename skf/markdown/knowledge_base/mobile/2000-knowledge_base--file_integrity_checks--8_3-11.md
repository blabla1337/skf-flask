## Description:

File Integrity Checks

MSTG-RESILIENCE-3: The app detects, and responds to, tampering with executable files and critical data within its own sandbox.

MSTG-RESILIENCE-11: All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data.

There are two topics related to file integrity:

	1. _Code integrity checks:_ Reverse engineers can bypass application signature checks by re-packaging and re-signing an app using a developer or enterprise certificate. One way to make this harder is to add a custom check that determines whether the signatures still match at runtime.
	2. _The file storage integrity checks:_ Files are stored by the application should be protected.


## Mitigation:

Integrify of files are stored or used by the application should be protected and checked.
