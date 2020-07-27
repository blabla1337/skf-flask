##Description:

The software makes an explicit call to the finalize() method from outside the finalizer.

While the Java Language Specification allows an object's finalize() method to be called from outside the finalizer, doing so is usually a bad idea. For example, calling finalize() explicitly means that finalize() will be called more than once: the first time will be the explicit call and the last time will be the call that is made after the object is garbage collected.

##Mitigation:


PHASE:Implementation Testing:
Do not make explicit calls to finalize(). Use static analysis tools to spot such instances.

