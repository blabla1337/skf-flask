### Double-free and Use-after-free

[Memory-unsafe code]

Out-of-bounds reads and writes are not the only problem for programs written in languages like C or C++.

When processing information you typically need to allocate memory (e.g., with **new**) and use it for a while. Most programming languages automatically track when you don’t need to use memory any more and reclaim it; this process is called *automatic garbage collection* or *automated memory management* (we will use the latter term). There are different ways to do automated memory management (the most typical are reference counting or tracing), and terminology varies, but the point is that in most programming languages this is automatically handled for you.

But in some programming languages you must *manually* release memory when you are done with it. In particular, this is true for C (**free**) and C++ (**delete**). If you forget to release the memory when you are done using it, this leads to a “memory leak"; the program will increasingly use more memory. In some situations this increasing memory use can lead to a crash, which by definition is a loss of availability. But in security the bigger issue is usually freeing the memory region *more* than once; this is called a *double free*. Another big security problem is *use-after-free*, that is, using the memory after it has been freed. In memory-safe languages a double-free or use-after-free won’t happen. However, a double-free or use-after-free in a C or C++ program often corrupts low-level infrastructure and can change the value of program values that *appear* to be unrelated.

If an attacker can cause your program to double-free or use-after-free, this can result in a serious vulnerability where the attacker can cause the program to do anything. That is because these mistakes often allow an attacker to corrupt and control the infrastructure your program runs on.

The obvious solution is to only use programming languages where you don’t have to manually release memory; most languages handle this automatically.

In cases where that is not practical, simplify your code as best you can so that it is clear where deallocation will occur, so that it will occur exactly once and you never use it again. Consider setting pointers to NULL (0) when you are done with what they point to. This will reduce the risk of freeing them or using them again later, and if unnecessary many of those assignments will be optimized away by the compiler.

Use-after-free is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #7. It is [CWE-416](https://cwe.mitre.org/data/definitions/416.html) (*Use After Free*). Double-free is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #31. It is [CWE-415](https://cwe.mitre.org/data/definitions/415.html) (*Double Free*).