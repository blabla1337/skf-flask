## Description:

Sensitive Functionality Exposure Through IPC

MSTG-PLATFORM-4: The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.

During implementation of a mobile application, developers may apply traditional techniques for IPC (such as using shared files or network sockets). The IPC system functionality offered by mobile application platforms should be used because it is much more mature than traditional techniques. Using IPC mechanisms with no security in mind may cause the application to leak or expose sensitive data.

The following is a list of Android IPC Mechanisms that may expose sensitive data:

	- [Binders](https://developer.android.com/reference/android/os/Binder.html "IPCBinder")
	- [Services](https://developer.android.com/guide/components/services.html "IPCServices")
	- [Bound Services](https://developer.android.com/guide/components/bound-services.html "BoundServices")
	- [AIDL](https://developer.android.com/guide/components/aidl.html "AIDL")
	- [Intents](https://developer.android.com/reference/android/content/Intent.html "IPCIntent")
	- [Content Providers](https://developer.android.com/reference/android/content/ContentProvider.html "IPCContentProviders")

In contrast to Android's rich Inter-Process Communication (IPC) capability, iOS offers some rather limited options for communication between apps. In fact, there's no way for apps to communicate directly. Different types of indirect communication offered by iOS:

	- Custom URL Schemes
	- Universal Links
	- UIActivity Sharing
	- App Extensions
	- UIPasteboard


## Mitigation:

Identify all IPC mechanisms, review the source code to see whether sensitive data is leaked when the mechanisms are used. For example, content providers can be used to access database information, and services can be probed to see if they return data. Broadcast receivers can leak sensitive information if probed or sniffed.
