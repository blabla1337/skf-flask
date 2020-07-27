##Description:

whenever files from untrusted services are uploaded to the server, there should be additional checks
in place to verify whether these files contain viruses (malware, trojans, ransomware). 

## Solution:

After uploading the file, the file should be placed in quarantine and antivirus has to 
inspect the file for malicious viruses. Antivirus software that has a command-line interface is 
requisite for doing such scans. There are also API's available for other services such as
from "VirusTotal.com" 

This site provides a free service in which your file is given as input to 
numerous antivirus products and you receive back a detailed report with the evidence resulting from 
the scanning process
