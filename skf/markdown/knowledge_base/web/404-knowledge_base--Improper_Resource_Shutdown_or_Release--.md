##Description:

The program does not release or incorrectly releases a resource before it is made available for re-use.

When a resource is created or allocated, the developer is responsible for properly releasing the resource as well as accounting for all potential paths of expiration or invalidation, such as a set period of time or revocation.

##Mitigation:


PHASE:Requirements:STRATEGY:Language Selection:
Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, languages such as Java, Ruby, and Lisp perform automatic garbage collection that releases memory for objects that have been deallocated.

PHASE:Implementation:
It is good practice to be responsible for freeing all resources you allocate and to be consistent with how and where you free memory in a function. If you allocate memory that you intend to free upon completion of the function, you must be sure to free the memory at all exit points for that function including error conditions.

PHASE:Implementation:
Memory should be allocated/freed using matching functions such as malloc/free, new/delete, and new[]/delete[].

PHASE:Implementation:
When releasing a complex object or structure, ensure that you properly dispose of all of its member components, not just the object itself.

