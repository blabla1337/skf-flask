## Description:

Device Binding

MSTG-RESILIENCE-10: The app implements a 'device binding' functionality using a device fingerprint derived from multiple properties unique to the device.

The goal of device binding is to impede an attacker who tries to both copy an app and its state from device A to device B and continue executing the app on device B. After device A has been determined trustworthy, it may have more privileges than device B. These differential privileges should not change when an app is copied from device A to device B.


## Mitigation:

Make sure Device Binding depends on uniqe device properties and those values can not be changed.

For example, IMEI numbers are unique for each mobile devices, however users can manipulate them. Therefore, it is not a great option for binding purposes.