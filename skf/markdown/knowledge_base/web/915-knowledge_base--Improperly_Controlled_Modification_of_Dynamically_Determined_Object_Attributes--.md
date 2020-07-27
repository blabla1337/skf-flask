##Description:

The software receives input from an upstream component that specifies multiple attributes, properties, or fields that are to be initialized or updated in an object, but it does not properly control which attributes can be modified.

If the object contains attributes that were only intended for internal use, then their unexpected modification could lead to a vulnerability. This weakness is sometimes known by the language-specific mechanisms that make it possible, such as mass assignment, autobinding, or object injection.

##Mitigation:


PHASE:Implementation:
If available, use features of the language or framework that allow specification of whitelists of attributes or fields that are allowed to be modified. If possible, prefer whitelists over black lists. For applications written with Ruby on Rails, use the attr_accessible (whitelist) or attr_protected (blacklist) macros in each class that may be used in mass assignment.

PHASE:Architecture and Design Implementation:
If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.

PHASE:Implementation:STRATEGY:Input Validation:
For any externally-influenced input, check the input against a white list of internal object attributes or fields that are allowed to be modified.

PHASE:Implementation Architecture and Design:STRATEGY:Refactoring:
Refactor the code so that object attributes or fields do not need to be dynamically identified, and only expose getter/setter functionality for the intended attributes.

