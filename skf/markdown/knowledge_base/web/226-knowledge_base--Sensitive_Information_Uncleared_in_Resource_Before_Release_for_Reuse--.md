##Description:

The product prepares to release a resource such as memory or a file so that the resource can be reused by other entities, but the product does not fully clear previously-used sensitive information from that resource before the resource is released.

When resources are released, they can be made available to other parties for reuse. For example, after memory is used and released, an operating system may make the memory available to another process, or disk space may be reallocated when a file is deleted. It is not necessarily guaranteed that the operating system will re-initialize the resource or otherwise remove the original contents. Even when the resource is reused by the same process, this weakness can arise when new data is not as large as the old data, which leaves portions of the old data still available. Equivalent errors can occur in other situations where the length of data is variable but the associated data structure is not. If memory is not cleared after use, it may allow unintended actors to read the data when the memory is reallocated.

##Mitigation:
