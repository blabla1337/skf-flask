# CODEQL
-------

## Example:

        Lang support:
        Go, Java, JavaScript, TypeScript, Python, C, C++, C#

        - CodeQL is the industry-leading semantic code analysis engine.
        - CodeQL lets you query code as though it were data.
        - Write a query to find all variants of a vulnerability, using an object-oriented logic programming language, and reusing built-in libraries for data flow and taint tracking analysis. 
        - Then share your query to help others do the same, by contributing to the open source repository.

        CodeQL is free for research and open source.

        Out of the box, CodeQL provides a standard set of queries created by GitHub, language experts, and security researchers. As the queries are open source, the community maintains and updates them to improve analysis and reduce false positives.

        Example: [Client-side cross-site scripting in JavaScript](https://lgtm.com/rules/2022121412/)
        ```
        import javascript
        import semmle.javascript.security.dataflow.DomBasedXss::DomBasedXss
        import DataFlow::PathGraph

        from Configuration cfg, DataFlow::PathNode source, DataFlow::PathNode sink
        where cfg.hasFlowPath(source, sink)
        select sink.getNode(), source, sink,
            sink.getNode().(Sink).getVulnerabilityKind() + " vulnerability due to $@.", source.getNode(),
            "user-provided value"
        ```

        You can benefit from the power of the CodeQL analysis on your GitHub repository with GitHub code scanning. Just visit ["Enabling code scanning for a repository"](https://docs.github.com/en/free-pro-team@latest/github/finding-security-vulnerabilities-and-errors-in-your-code/enabling-code-scanning-for-a-repository), to get the standard set of CodeQL queries protecting your code, on a given schedule, or during a Pull Request, so that the vulnerability never reaches your main branch. 

        [link to CodeQL](https://codeql.com)

        [link to CodeQL open source queries](https://github.com/codeql)

        [link to CodeQL open source queries for GO](https://github.com/github/codeql-go)
