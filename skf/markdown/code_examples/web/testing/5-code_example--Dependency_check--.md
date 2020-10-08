# OWASP Dependency check
-------

## Example:

        Dependency-Check is a Software Composition Analysis (SCA) tool that attempts to detect 
        publicly disclosed vulnerabilities contained within a project’s dependencies. It does 
        this by determining if there is a Common Platform Enumeration (CPE) identifier for a 
        given dependency. If found, it will generate a report linking to the associated CVE entries.

        Dependency-check has a command line interface, a Maven plugin, an Ant task, 
        and a Jenkins plugin. The core engine contains a series of analyzers that inspect the 
        project dependencies, collect pieces of information about the dependencies 
        (referred to as evidence within the tool). The evidence is then used to identify the 
        Common Platform Enumeration (CPE) for the given dependency. If a CPE is identified, a 
        listing of associated Common Vulnerability and Exposure (CVE) entries are listed in a report. 
        Other 3rd party services and data sources such as the NPM Audit API, the OSS Index, 
        RetireJS, and Bundler Audit are utilized for specific technologies.

        [Dependency check project page](https://owasp.org/www-project-dependency-check/)
