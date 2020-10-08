# SEMGREP
-------

## Example:

    Lang support:
    Go, Java, JavaScript, JSON, Python, Ruby (beta,) C (alpha), OCaml (alpha)

    - A simple, customizable, and fast static analysis tool for finding bugs
    - Combines the speed and customizability of grep with the precision of traditional static analysis tools
    - No painful domain-specific language; Semgrep rules look like the source code you’re targeting
    - Runs offline on uncompiled code in CI, at pre-commit, or in the editor
    - Open-source maintained and commercially supported by r2c

    Out of the box Semgrep has a good ruleset but the trick is to write
    your own to automatically govern your ASVS controls.

    Rule example python:
    ```
    rules:
    - id: unsafe-exec
      pattern: |
        exec(...);
      message: |
        Avoid use of exec; it can lead to a remote code execution.
      fix: |
        
      severity: WARNING
      ```


    Follow the link to find more rule-sets, how to run semgrep on
    PR's in CI.

    [link to Semgrep](https://semgrep.dev/)

    [link to Semgrep Github](https://github.com/returntocorp/semgrep)