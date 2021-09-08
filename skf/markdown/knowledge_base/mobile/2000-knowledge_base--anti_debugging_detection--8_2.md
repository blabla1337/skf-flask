## Description:

Anti-Debugging Detection

MSTG-RESILIENCE-2: The app prevents debugging and/or detects, and responds to, a debugger being attached. All available debugging protocols must be covered.

Debugging is a highly effective way to analyze runtime app behavior. It allows the reverse engineer to step through the code, stop app execution at arbitrary points, inspect the state of variables, read and modify memory, and a lot more.

Anti-debugging features can be preventive or reactive. As the name implies, preventive anti-debugging prevents the debugger from attaching in the first place; reactive anti-debugging involves detecting debuggers and reacting to them in some way (e.g., terminating the app or triggering hidden behavior). The "more-is-better" rule applies: to maximize effectiveness, defenders combine multiple methods of prevention and detection that operate on different API layers and are well distributed throughout the app.

Application developers of apps processing highly sensitive data should be aware of the fact that preventing debugging is virtually impossible. If the app is publicly available, it can be run on an untrusted device, that is under full control of the attacker. A very determined attacker will eventually manage to bypass all the app's anti-debugging controls by patching the app binary or by dynamically modifying the app's behavior at runtime with tools such as Frida.


## Mitigation:

Implement a proper anti-debugging mechanisms. 
