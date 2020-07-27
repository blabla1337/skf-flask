##Description:

The software sets a pointer to a specific address other than NULL or 0.

Using a fixed address is not portable because that address will probably not be valid in all environments or platforms.

##Mitigation:


PHASE:Implementation:
Never set a pointer to a fixed address.

