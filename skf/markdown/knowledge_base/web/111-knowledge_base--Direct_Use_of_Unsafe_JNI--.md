##Description:

When a Java application uses the Java Native Interface (JNI) to call code written in another programming language, it can expose the application to weaknesses in that code, even if those weaknesses cannot occur in Java.

Many safety features that programmers may take for granted simply do not apply for native code, so you must carefully review all such code for potential problems. The languages used to implement native code may be more susceptible to buffer overflows and other attacks. Native code is unprotected by the security features enforced by the runtime environment, such as strong typing and array bounds checking.

##Mitigation:


PHASE:Implementation:
Implement error handling around the JNI call.

PHASE:Implementation:STRATEGY:Refactoring:
Do not use JNI calls if you don't trust the native library.

PHASE:Implementation:STRATEGY:Refactoring:
Be reluctant to use JNI calls. A Java API equivalent may exist.

