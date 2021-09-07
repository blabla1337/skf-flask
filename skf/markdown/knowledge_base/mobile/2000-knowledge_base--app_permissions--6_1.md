## Description:

App Permissions

MSTG-PLATFORM-1: The app only requests the minimum set of permissions necessary.

Android assigns a distinct system identity (Linux user ID and group ID) to every installed app. Because each Android app operates in a process sandbox, apps must explicitly request access to resources and data that are outside their sandbox. They request this access by declaring the permissions they need to use system data and features. Depending on how sensitive or critical the data or feature is, the Android system will grant the permission automatically or ask the user to approve the request.

Android permissions are classified into four different categories on the basis of the protection level they offer:

	- Normal: This permission gives apps access to isolated application-level features with minimal risk to other apps, the user, and the system. For apps targeting Android 6.0 (API level 23) or higher, these permissions are granted automatically at installation time. For apps targeting a lower API level, the user needs to approve them at installation time. Example: `android.permission.INTERNET`.
	- Dangerous: This permission usually gives the app control over user data or control over the device in a way that impacts the user. This type of permission may not be granted at installation time; whether the app should have the permission may be left for the user to decide. Example: `android.permission.RECORD_AUDIO`.
	- Signature: This permission is granted only if the requesting app was signed with the same certificate used to sign the app that declared the permission. If the signature matches, the permission will be granted automatically. This permission is granted at installation time. Example: `android.permission.ACCESS_MOCK_LOCATION`.
	- SystemOrSignature: This permission is granted only to applications embedded in the system image or signed with the same certificate used to sign the application that declared the permission. Example: `android.permission.ACCESS_DOWNLOAD_MANAGER`.

A list of all permissions can be found in the [Android developer documentation](https://developer.android.com/guide/topics/permissions/overview.html "Permissions overview") as well as concrete steps on how to:
```
	- [Declare app permissions](https://developer.android.com/training/permissions/declaring) in your app's manifest file.
	- [Request app permissions](https://developer.android.com/training/permissions/requesting) programatically.
	- [Define a Custom App Permission](https://developer.android.com/guide/topics/permissions/defining) to share your app resources and capabilities with other apps.
```
In contrast to Android, where each app runs on its own user ID, iOS makes all third-party apps run under the non-privileged `mobile` user. Each app has a unique home directory and is sandboxed, so that they cannot access protected system resources or files stored by the system or by other apps. These restrictions are implemented via sandbox policies (aka. *profiles*), which are enforced by the [Trusted BSD (MAC) Mandatory Access Control Framework](http://www.trustedbsd.org/mac.html "TrustedBSD Mandatory Access Control (MAC) Framework") via a kernel extension. iOS applies a generic sandbox profile to all third-party apps called *container*. Access to protected resources or data (some also known as [app capabilities](https://developer.apple.com/support/app-capabilities/ "Advanced App Capabilities")) is possible, but it's strictly controlled via special permissions known as *entitlements*.

Some permissions can be configured by the app's developers (e.g. Data Protection or Keychain Sharing) and will directly take effect after the installation. However, for others, the user will be explicitly asked the first time the app attempts to access a protected resource, [for example](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/ExpectedAppBehaviors/ExpectedAppBehaviors.html#//apple_ref/doc/uid/TP40007072-CH3-SW7 "Data and resources protected by system authorization settings"):

	- Bluetooth peripherals
	- Calendar data
	- Camera
	- Contacts
	- Health sharing
	- Health updating
	- HomeKit
	- Location
	- Microphone
	- Motion
	- Music and the media library
	- Photos
	- Reminders
	- Siri
	- Speech recognition
	- the TV provider


## Mitigation:

Check permissions to make sure that the app really needs them and remove unnecessary permissions. The developer should check whether the application has the appropriate permission each time an action is performed that would require that permission.
