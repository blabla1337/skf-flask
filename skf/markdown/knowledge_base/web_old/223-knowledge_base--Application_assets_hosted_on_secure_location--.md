##Description:

Whenever application assets such as JavaScript libraries or CSS styleshees are not hosted
on the application itself but on a external CDN which is not under your control these
CDNs' can introduce security vulnerabilities. Whenever one of these CDN gets compromised
attackers can include malicious scripts. Also whenever one of these CDNs' get out of service
it could affect the operation of the application and even cause a denial of service.

## Solution:

Verify that all application assets are hosted by the application, such as JavaScript libraries, CSS
stylesheets and web fonts are hosted by the application rather than rely on a CDN or external
provider. 
