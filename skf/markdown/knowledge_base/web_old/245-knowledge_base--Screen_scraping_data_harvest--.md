##Description:

Whenever the application does not put a threshold on the number requests made to the server,
screen scraping and data harvesting tools can gather data and information.

i.e should the application contain an insecure direct object reference, then the data harvesting
tool could now harvest information it was not originally authorized to access to.

Or the application is a web shop and the competition is scraping prices and products in order to 
give them an edge on comparison websites and get more business.

##Mitigation:

ModSecurity can be used to set up rules to prevent attackers from scraping and harvesting data
from the application. The ModSecurity can be set up with thresholds and rate limiting and block
IP adresses if they exceed the threshold.
