# Question
 
What is the problem here?
 
```
void WebPagetoVisit (string url)
{
        if (url == null)
                throw new ArgumentNullException ("url");
        if (url.IndexOf ('\n') != -1)
                throw new ArgumentException ("Redirect URI cannot contain newline characters.", "url");
                
        bool isFullyQualified;
        if (StrUtils.StartsWith (url, "http:", true) ||
            StrUtils.StartsWith (url, "https:", true) ||
            StrUtils.StartsWith (url, "file:", true) ||
            StrUtils.StartsWith (url, "ftp:", true))
                isFullyQualified = true;
        else
                isFullyQualified = false;
        if (isFullyQualified) {
                redirect_location = url;
                Write ("<html><head><title>Object moved</title></head><body>\r\n");
                Write ("<h2>Object moved to <a href=\"" + url + "\">here</a></h2>\r\n");
                Write ("</body><html>\r\n");
        }
        else {
                Write ("<html><head><title>Url address error</title></head><body>\r\n");
                Write ("<h2>The Url address you provided " + url + " is not valid!</h2>\r\n");
                Write ("</body><html>\r\n");
        }
}
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'url' parameter is vulnerable for malicious injection and no input sanitization is being in use. Injected javascript codes will be executed in the response.
