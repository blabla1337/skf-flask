## Description:

Reverse tabnabbing is an attack where a page linked from the target page is able to rewrite that page, 
for example to replace it with a phishing site. As the user was originally on the correct page they are 
less likely to notice that it has been changed to a phishing site, especially it the site looks the same as the target. 
If the user authenticates to this new page then their credentials (or other sensitive data) are sent to the phishing site 
rather than the legitimate one.

As well as the target site being able to overwrite the target page, any http link can be spoofed to overwrite the target 
page if the user is on an unsecured network, for example a public wifi hotspot. The attack is possible even if the target 
site is only available via https as the attacker only needs to spoof the http site that is being linked to.

## Solution:

To prevent this issue the following actions are available:

Cut the back link between the parent and the child pages:
 - For html link:
   * To cut this back link then add the attribute rel="noopener" on the 
     tag used to create the link from the parent page to the child page. 
     This attribute value cut the link but, depending on the browser, let referrer
     information be present in the request to the child page.
   * To remove also the referrer information then use this attribute value: rel="noopener noreferrer".
 - For javascript window.open function, add the values noopener,noreferrer in the windowFeatures parameter of the window.open function.

As the behavior using the elements above is different between the browsers either using html 
link or javascript to open a window (or tab) then use this configuration to maximize the cross supports:

* For html link, add the attribute rel="noopener noreferrer" for every links.
* For Javascript, use this function to open a window (or tab):

  function openPopup(url, name, windowFeatures){
    //Open the popup and set the opener and referrer policy instruction
    var newWindow = window.open(url, name, 'noopener,noreferrer,' + windowFeatures);
    //Reset the opener link
    newWindow.opener = null;
  }
  
Add the HTTP response header Referrer-Policy: no-referrer the every HTTP responses send by the application
(Header Referrer-Policy information). This configuration will ensure that no referrer information is sent 
along with requests from page.
