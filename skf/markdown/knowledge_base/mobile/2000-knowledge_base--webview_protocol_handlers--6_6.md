## Description:

WebView Protocol Handlers

MSTG-PLATFORM-6: WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and app-id, are disabled.

Several default schemas are available for both IOS and Android URLs. They can be triggered within a WebView with the following:

	- http(s)://
	- file://
	- tel://

WebViews can load remote content from an endpoint, but they can also load local content from the app data directory or storage. If the local content is loaded, the user shouldn't be able to influence the filename or the path used to load the file, and users shouldn't be able to edit the loaded file.


## Mitigation:

Use the following best practices as defensive-in-depth measures:
	- Create a list that defines local and remote web pages and URL schemes that are allowed to be loaded.
	- Create checksums of the local HTML/JavaScript files and check them while the app is starting up. [Minify JavaScript files](https://en.wikipedia.org/wiki/Minification_%28programming%29) "Minification (programming)") to make them harder to read.
