##Description:

The software uses or accesses a file descriptor after it has been closed.

After a file descriptor for a particular file or device has been released, it can be reused. The code might not write to the original file, since the reused file descriptor might reference a different file or device.

##Mitigation:
