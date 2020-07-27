##Description:

The software receives data from an upstream component, but only accounts for special elements at a specified location, thereby missing remaining special elements that may exist before sending it to a downstream component.

A filter might only account for instances of special elements when they occur: relative to a marker (e.g. at the beginning/end of string; the second argument), or at an absolute position (e.g. byte number 10). This may leave special elements in the data that did not match the filter position, but still may be dangerous.

##Mitigation:
