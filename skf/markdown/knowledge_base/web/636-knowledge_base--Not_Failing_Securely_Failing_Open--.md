##Description:

When the product encounters an error condition or failure, its design requires it to fall back to a state that is less secure than other options that are available, such as selecting the weakest encryption algorithm or using the most permissive access control restrictions.

By entering a less secure state, the product inherits the weaknesses associated with that state, making it easier to compromise. At the least, it causes administrators to have a false sense of security. This weakness typically occurs as a result of wanting to fail functional to minimize administration and support costs, instead of failing safe.

##Mitigation:


PHASE:Architecture and Design:
Subdivide and allocate resources and components so that a failure in one part does not affect the entire product.

