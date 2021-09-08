## Description:

Finding Debugging Symbols

MSTG-CODE-3: Debugging symbols have been removed from native binaries.

Generally, as little explanatory information as possible should be provided with the compiled code. Some metadata (such as debugging information, line numbers, and descriptive function or method names) makes the binary or bytecode easier for the reverse engineer to understand but isn't necessary in a release build. This metadata can therefore be discarded without impacting the app's functionality.


## Mitigation:

Decompiling bytecode and libraries help to make sure that unnecessary metadata has been discarded.