## Description:

JavaScript Execution in WebViews

MSTG-PLATFORM-5: JavaScript is disabled in WebViews unless explicitly required.

WebViews are in-app browser components for displaying interactive web content. They can be used to embed web content directly into an app's user interface. 

JavaScript can be injected into web applications via reflected, stored, or DOM-based Cross-Site Scripting (XSS). Mobile apps are executed in a sandboxed environment and don't have this vulnerability when implemented natively. Nevertheless, WebViews may be part of a native app to allow web page viewing. Every app has its own WebView cache, which isn't shared with the native Browser or other apps. On Android, WebViews use the WebKit rendering engine to display web pages, but the pages are stripped down to minimal functions, for example, pages don't have address bars. If the WebView implementation is too lax and allows usage of JavaScript, JavaScript can be used to attack the app and gain access to its data. iOS WebViews also support JavaScript execution by default, so script injection and Cross-Site Scripting attacks can affect them.


## Mitigation:

If JavaScript is necessary, you should make sure that:

	- Identifying WebView usage
	- Testing JavaScript configuration
	- Testing for mixed content
	- Testing for WebView URI manipulation
	- The communication to the endpoints consistently relies on HTTPS (or other protocols that allow encryption) to protect HTML and JavaScript from tampering during transmission.
	- JavaScript and HTML are loaded locally, from within the app data directory or from trusted web servers only.
	- The user cannot define which sources to load by means of loading different resources based on a user provided input.
