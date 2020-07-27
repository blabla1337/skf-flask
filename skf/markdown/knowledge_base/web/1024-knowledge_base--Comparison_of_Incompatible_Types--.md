##Description:

The software performs a comparison between two entities, but the entities are of different, incompatible types that cannot be guaranteed to provide correct results when they are directly compared.

In languages that are strictly typed but support casting/conversion, such as C or C++, the programmer might assume that casting one entity to the same type as another entity will ensure that the comparison will be performed correctly, but this cannot be guaranteed. In languages that are not strictly typed, such as PHP or JavaScript, there may be implicit casting/conversion to a type that the programmer is unaware of, causing unexpected results; for example, the string 123 might be converted to a number type. See examples.

##Mitigation:


PHASE:Testing:
Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

