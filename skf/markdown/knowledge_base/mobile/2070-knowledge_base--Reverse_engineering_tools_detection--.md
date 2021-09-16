## Description:

Reverse Engineering Tools Detection

MSTG-RESILIENCE-4: The app detects, and responds to, the presence of widely used reverse engineering tools and frameworks on the device.

The presence of tools, frameworks and apps commonly used by reverse engineers may indicate an attempt to reverse engineer the app. Some of these tools can only run on a jailbroken/rooted device, while others force the app into debugging mode or depend on starting a background service on the mobile phone. Therefore, there are different ways that an app may implement to detect a reverse engineering attack and react to it, e.g. by terminating itself.


## Mitigation:

You can detect popular reverse engineering tools (for example Frida, Cydia, Substrate, Cycript, Xposed, etc.) that have been installed in an unmodified form by looking for associated application packages, files, processes, or other tool-specific modifications and artifacts.