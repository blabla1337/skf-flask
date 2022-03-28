# Question
 
What is the problem here?
 
```
#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv) {
    char cat[] = "cat ";
    char *command;
    size_t commandLength;
    commandLength = strlen(cat) + strlen(argv[1]) + 1;
    command = (char *) malloc(commandLength);
    strncpy(command, cat, commandLength);
    strncat(command, argv[1], (commandLength - strlen(cat)) );
    system(command);
    return (0);
}
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. The code is a wrapper around the UNIX command cat which prints the contents of a file to standard output. However, it is vulnerable for command injections. For example: '$ ./catWrapper "Story.txt; ls"' will return file content and directory listing. https://owasp.org/www-community/attacks/Command_Injection