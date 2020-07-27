##Description:

If the application logic transmits session IDs in the URL, their values could be leaked through the Referer header to third-party websites, logged by proxy servers, bookmarked in the browser, accidentally sent via emails or chats. 
Whenever the session ID is disclosed in the URL there might be also the possibility to perform other attacks (like session fixation) that lead to session hijacking.

## Solution:

Session tokens should never be included in places other than the application Cookie header or other custom headers defined by the application.

