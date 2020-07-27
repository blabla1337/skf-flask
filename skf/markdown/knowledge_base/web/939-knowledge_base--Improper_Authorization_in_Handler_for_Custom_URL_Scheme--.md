##Description:

The software uses a handler for a custom URL scheme, but it does not properly restrict which actors can invoke the handler using the scheme.

Mobile platforms and other architectures allow the use of custom URL schemes to facilitate communication between applications. In the case of iOS, this is the only method to do inter-application communication. The implementation is at the developer's discretion which may open security flaws in the application. An example could be potentially dangerous functionality such as modifying files through a custom URL scheme.

##Mitigation:


PHASE:Architecture and Design:
Utilize a user prompt pop-up to authorize potentially harmful actions such as those modifying data or dealing with sensitive information. When designing functionality of actions in the URL scheme, consider whether the action should be accessible to all mobile applications, or if a whitelist of applications to interface with is appropriate.

