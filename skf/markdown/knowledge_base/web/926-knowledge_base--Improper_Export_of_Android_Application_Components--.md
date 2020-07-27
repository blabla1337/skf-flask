##Description:

The Android application exports a component for use by other applications, but does not properly restrict which applications can launch the component or access the data it contains.

The attacks and consequences of improperly exporting a component may depend on the exported component: If access to an exported Activity is not restricted, any application will be able to launch the activity. This may allow a malicious application to gain access to sensitive information, modify the internal state of the application, or trick a user into interacting with the victim application while believing they are still interacting with the malicious application. If access to an exported Service is not restricted, any application may start and bind to the Service. Depending on the exposed functionality, this may allow a malicious application to perform unauthorized actions, gain access to sensitive information, or corrupt the internal state of the application. If access to a Content Provider is not restricted to only the expected applications, then malicious applications might be able to access the sensitive data. Note that in Android before 4.2, the Content Provider is automatically exported unless it has been explicitly declared as NOT exported.

##Mitigation:


PHASE:Build and Compilation:STRATEGY:Attack Surface Reduction:
If they do not need to be shared by other applications, explicitly mark components with android:exported=false in the application manifest.

PHASE:Build and Compilation:STRATEGY:Attack Surface Reduction:
If you only intend to use exported components between related apps under your control, use android:protectionLevel=signature in the xml manifest to restrict access to applications signed by you.

PHASE:Build and Compilation Architecture and Design:STRATEGY:Attack Surface Reduction:
Limit Content Provider permissions (read/write) as appropriate.

PHASE:Build and Compilation Architecture and Design:STRATEGY:Separation of Privilege:
Limit Content Provider permissions (read/write) as appropriate.

