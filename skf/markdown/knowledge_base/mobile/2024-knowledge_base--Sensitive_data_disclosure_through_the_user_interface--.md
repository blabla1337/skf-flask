## Description:

Sensitive Data Disclosure Through the User Interface

MSTG-STORAGE-7: No sensitive data, such as passwords or pins, is exposed through the user interface.

Entering sensitive information when, for example, registering an account or making payments, is an essential part of using many apps. This data may be financial information such as credit card data or user account passwords. The data may be exposed if the app doesn't properly mask it while it is being typed.


## Mitigation:

Masking of sensitive data, by showing asterisk or dots instead of clear text should be enforced within an app's activity to prevent disclosure and mitigate risks such as shoulder surfing.