# Question
 
What is the problem here?
 
```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char **argv)
{
    char command[256];
    if(argc != 2) {
        printf("Error: Please enter a program to time!\n");
        return -1;
    }
    memset(&command, 0, sizeof(command));
    strcat(command, "time ./");
    strcat(command, argv[1]);
    system(command);
    return 0;
}
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. The code snippet is vulnerable to OS command injection on the Unix/Linux platforms. If this were a suid binary, consider the case when an attacker enters the following: 'ls; cat /etc/shadow'. In the Unix environment, shell commands are separated by a semi-colon. We now can execute system commands at will! https://owasp.org/www-community/attacks/Command_Injection