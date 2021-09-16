## Description:

Determining Whether Java Objects/Native Methods Are Exposed Through WebViews

MSTG-PLATFORM-7: If native methods of the app are exposed to a WebView, verify that the WebView only renders JavaScript contained within the app package.

Since iOS 7, Apple introduced APIs that allow communication between the JavaScript runtime in the WebView and the native Swift or Objective-C objects. If these APIs are used carelessly, important functionality might be exposed to attackers who manage to inject malicious scripts into the WebView (e.g., through a successful Cross-Site Scripting attack).

Android offers a way for JavaScript executed in a WebView to call and use native functions of an Android app (annotated with `@JavascriptInterface`) by using the [`addJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView.html#addJavascriptInterface%28java.lang.Object,%20java.lang.String%29 "Method addJavascriptInterface()") method. This is known as a _WebView JavaScript bridge_ or _native bridge_.


## Mitigation:

You need to determine how methods are used, and whether an attacker can inject malicious JavaScript.

Only JavaScript provided with the app should be allowed to use the bridges.

No JavaScript should be loaded from remote endpoints, e.g. by keeping page navigation within the app's domains and opening all other domains on the default browser (e.g. Chrome, Firefox).