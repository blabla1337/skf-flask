##Description:

The software uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize absolute path sequences such as /abs/path that can resolve to a location that is outside of that directory.

This allows attackers to traverse the file system to access files or directories that are outside of the restricted directory.

##Mitigation:
