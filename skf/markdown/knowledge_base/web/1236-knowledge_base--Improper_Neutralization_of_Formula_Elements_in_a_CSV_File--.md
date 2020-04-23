## Description:

The software saves user-provided information into a Comma-Separated Value (CSV) file, but it does not neutralize or incorrectly neutralizes special elements that could be interpreted as a command when the file is opened by spreadsheet software.

User-provided data is often saved to traditional databases. This data can be exported to a CSV file, which allows users to read the data using spreadsheet software such as Excel, Numbers, or Calc. This software interprets entries beginning with '=' as formulae, which are then executed by the spreadsheet software. The software's formula language often allows methods to access hyperlinks or the local command line, and frequently allows enough characters to invoke an entire script. Attackers can populate data fields which, when saved to a CSV file, may attempt information exfiltration or other malicious activity when automatically executed by the spreadsheet software.

## Mitigation:


PHASE:Implementation:
When generating CSV output, ensure that formula-sensitive metacharacters are effectively escaped or removed from all data before storage in the resultant CSV. Risky characters include '=' (equal), '+' (plus), '-' (minus), and '@' (at).:EFFECTIVENESS:Moderate

PHASE:Implementation:
If a field starts with a formula character, prepend it with a ' (single apostrophe), which prevents Excel from executing the formula.:EFFECTIVENESS:Moderate

PHASE:Architecture and Design:
Certain implementations of spreadsheet software might disallow formulae from executing if the file is untrusted, or if the file is not authored by the current user.:EFFECTIVENESS:Limited

