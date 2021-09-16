## Description:

WebView sources should be cleared

MSTG-PLATFORM-10: A WebView’s cache, storage, and loaded resources (JavaScript, etc.) should be cleared before the WebView is destroyed.


## Mitigation:

Make sure all webView’s caches, storages, and loaded resources are cleared before destroying the instance.