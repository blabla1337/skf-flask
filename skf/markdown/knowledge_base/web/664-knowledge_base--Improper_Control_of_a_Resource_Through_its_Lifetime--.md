##Description:

The software does not maintain or incorrectly maintains control over a resource throughout its lifetime of creation, use, and release.

Resources often have explicit instructions on how to be created, used and destroyed. When software does not follow these instructions, it can lead to unexpected behaviors and potentially exploitable states. Even without explicit instructions, various principles are expected to be adhered to, such as Do not use an object until after its creation is complete, or do not use an object after it has been slated for destruction.

##Mitigation:


PHASE:Testing:
Use Static analysis tools to check for unreleased resources.

