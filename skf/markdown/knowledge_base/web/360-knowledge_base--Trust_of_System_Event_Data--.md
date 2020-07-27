##Description:

Security based on event locations are insecure and can be spoofed.

Events are a messaging system which may provide control data to programs listening for events. Events often do not have any type of authentication framework to allow them to be verified from a trusted source. Any application, in Windows, on a given desktop can send a message to any window on the same desktop. There is no authentication framework for these messages. Therefore, any message can be used to manipulate any process on the desktop if the process does not check the validity and safeness of those messages.

##Mitigation:


PHASE:Architecture and Design:
Never trust or rely any of the information in an Event for security.

