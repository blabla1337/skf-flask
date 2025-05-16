# Login Troubleshooting Guide

## Issue with Default Credentials

Several users have reported issues logging in with default credentials in the Docker deployment of this version of SKF (Issue #844).

## Important Notice

**This repository is archived and no longer actively maintained.**

The Security Knowledge Framework team is now developing a new version of the platform. For the latest updates and active development, please visit:

- [SKF Platform](https://github.com/Security-Knowledge-Framework/Platform)
- [SKF Requirements Tool](https://github.com/Security-Knowledge-Framework/SKF-requirements-tool)
- [SKF Labs](https://github.com/Security-Knowledge-Framework/Labs)

## Workaround for Login Issues

If you still need to use this version, here are some troubleshooting steps:

1. Check the docker-compose.yml file, which shows that the default environment variables are:
   - For MySQL: 
     - MYSQL_ROOT_PASSWORD: 'admin-skf-secret'
   - For the SKF Angular application:
     - SKIP_LOGIN=skiploginprovider

2. Try using the "Skip Login" feature:
   The docker-compose.yml file indicates a SKIP_LOGIN environment variable is set to "skiploginprovider". Look for this option on the login page.

3. If you need to create a custom user:
   Check the API documentation or source code for user creation endpoints.

## Recommended Solution

We recommend using the new version of SKF rather than troubleshooting this archived version. The new platform includes improvements to the authentication system and overall user experience.