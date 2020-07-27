##Description:

The program compares object references instead of the contents of the objects themselves, preventing it from detecting equivalent objects.

For example, in Java, comparing objects using == usually produces deceptive results, since the == operator compares object references rather than values; often, this means that using == for strings is actually comparing the strings' references, not their values.

##Mitigation:


PHASE:Implementation:
In Java, use the equals() method to compare objects instead of the == operator. If using ==, it is important for performance reasons that your objects are created by a static factory, not by a constructor.

