## Description:

Custom URL Schemes

MSTG-PLATFORM-3: The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.

Custom URL schemes [allow apps to communicate via a custom protocol](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6-SW1 "Using URL Schemes to Communicate with Apps"). An app must declare support for the schemes and handle incoming URLs that use those schemes.

Apple warns about the improper use of custom URL schemes in the [Apple Developer Documentation](https://developer.apple.com/documentation/uikit/core_app/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app "Defining a Custom URL Scheme for Your App"):

> URL schemes offer a potential attack vector into your app, so make sure to validate all URL parameters and discard any malformed URLs. In addition, limit the available actions to those that do not risk the user’s data. For example, do not allow other apps to directly delete content or access sensitive information about the user. When testing your URL-handling code, make sure your test cases include improperly formatted URLs.

They also suggest using universal links instead, if the purpose is to implement deep linking:

> While custom URL schemes are an acceptable form of deep linking, universal links are strongly recommended as a best practice.

Supporting a custom URL scheme is done by:
	- defining the format for the app's URLs,
	- registering the scheme so that the system directs appropriate URLs to the app,
	- handling the URLs that the app receives.

Security issues arise when an app processes calls to its URL scheme without properly validating the URL and its parameters and when users aren't prompted for confirmation before triggering an important action.

One example is the following [bug in the Skype Mobile app](http://www.dhanjani.com/blog/2010/11/insecure-handling-of-url-schemes-in-apples-ios.html "Insecure Handling of URL Schemes in Apple’s iOS"), discovered in 2010: The Skype app registered the `skype://` protocol handler, which allowed other apps to trigger calls to other Skype users and phone numbers. Unfortunately, Skype didn't ask users for permission before placing the calls, so any app could call arbitrary numbers without the user's knowledge. Attackers exploited this vulnerability by putting an invisible `<iframe src="skype://xxx?call"></iframe>` (where `xxx` was replaced by a premium number), so any Skype user who inadvertently visited a malicious website called the premium number.

As a developer, you should carefully validate any URL before calling it. You can allow only certain applications which may be opened via the registered protocol handler. Prompting users to confirm the URL-invoked action is another helpful control.

All URLs are passed to the app delegate, either at launch time or while the app is running or in the background. To handle incoming URLs, the delegate should implement methods to:
	- retrieve information about the URL and decide whether you want to open it,
	- open the resource specified by the URL.

More information can be found in the [archived App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6-SW13 "Handling URL Requests") and in the [Apple Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/ValidatingInput.html "Validating Input and Interprocess Communication").

In addition, an app may also want to send URL requests (aka. queries) to other apps. This is done by:
	- registering the application query schemes that the app wants to query,
	- optionally querying other apps to know if they can open a certain URL,
	- sending the URL requests.


Android allows you to create two different types of links for your apps: deep links and Android App Links. According to the [Android Developer Documentation](https://developer.android.com/training/app-links#app-links-vs-deep-links "Deep linking and Android App Links"), **deep links** are URLs that take users directly to specific content in your app. You can set up deep links by adding _intent filters_ and extracting data from incoming intents to drive users to the right activity. You can even use any custom scheme prefix such as `myapp`, which will result in the URI prefix "myapp://". These kind of deep links are also referred to as "Custom URL Schemes" and are typically used as a form of inter-app communication where an app can define certain actions (including the corresponding parameters) that can be triggered by other apps.

This method of defining deep links via intent filters has an important issue: any other apps installed on a user's device can declare and try to handle the same intent (typically a custom URL scheme). This is known as **deep link collision** where any arbitrary application can declare control over the exact same URL custom scheme belonging to another application. In recent versions of Android this results in a so-called _disambiguation dialog_ being shown to the user and asking them to select the application that should handle the link. The user could make the mistake of choosing a malicious application instead of the legitimate one.

Consider the following example of a deep link to an email application:

```default
emailapp://composeEmail/to=your.boss@company.com&message=SEND%20MONEY%20TO%20HERE!&sendImmediately=true
```

When a victim clicks such a link on a mobile device, a potentially vulnerable application might send an email from the user's original address containing attacker-crafted content. This could lead to financial loss, information disclosure, social damage of the victim, to name a few.

Another application specific example of deep linking is shown below:

```default
myapp://mybeautifulapp/endpoint?Whatismyname=MyNameIs<svg onload=alert(1)>&MyAgeIs=100
```

This deep link could be used in order to abuse some known vulnerabilities already identified within an application (e.g. via reverse engineering). For instance, consider an application running a WebView with JavaScript enabled and rendering the `Whatismyname` parameter. In this concrete case, the deep link payload would trigger reflected cross site scripting within the context of the WebView.

Since Android 6.0 (API Level 23) a developer can opt to define [**Android App Links**](https://developer.android.com/training/app-links/verify-site-associations "Verify Android App Links"), which are verified deep links based on a website URL explicitly registered by the developer. Clicking on an App Link will immediately open the app if it's installed and most importantly, **the disambiguation dialog won't be prompted** and therefore collisions are not possible anymore.

There are some key differences from _regular_ deep links to consider:
	- App Links only use `http://` and `https://` schemes, any other custom URL schemes are not allowed.
	- App Links require a live domain to serve a [Digital Asset Links file](https://developers.google.com/digital-asset-links/v1/getting-started "Digital Asset Link") via HTTPS.
	- App links do not suffer from deep link collision since they don't show a disambiguation dialog when a user opens them.

For every application, all existing deep links (including App Links) can potentially increase the app attack surface. All deep links must be enumerated and the actions they perform must be well tested, especially all input data which should be deemed to be untrustworthy and thus should be always validated. In addition, also consider the following:
	- When using reflection-based persistence type of data processing, check the section "Testing Object Persistence" for Android.
	- Using the data for queries? Make sure you make parameterized queries.
	- Using the data to do authenticated actions? Make sure that the user is in an authenticated state before the data is processed.
	- If tampering of the data will influence the result of the calculations: add an HMAC to the data.


## Mitigation:

Perform the following steps:
	- Testing custom URL schemes registration
	- Testing application query schemes registration
	- Testing URL handling and validation
	- Testing URL requests to other apps
	- Testing for deprecated methods