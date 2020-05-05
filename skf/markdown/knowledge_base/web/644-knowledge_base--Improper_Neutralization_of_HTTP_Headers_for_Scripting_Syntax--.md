## Description:

The application does not neutralize or incorrectly neutralizes web scripting syntax in HTTP headers that can be used by web browser components that can process raw headers, such as Flash.

An attacker may be able to conduct cross-site scripting and other attacks against users who have these components enabled. If an application does not neutralize user controlled data being placed in the header of an HTTP response coming from the server, the header may contain a script that will get executed in the client's browser context, potentially resulting in a cross site scripting vulnerability or possibly an HTTP response splitting attack. It is important to carefully control data that is being placed both in HTTP response header and in the HTTP response body to ensure that no scripting syntax is present, taking various encodings into account.

## Mitigation:


PHASE:Architecture and Design:
Perform output validation in order to filter/escape/encode unsafe data that is being passed from the server in an HTTP response header.

PHASE:Architecture and Design:
Disable script execution functionality in the clients' browser.

