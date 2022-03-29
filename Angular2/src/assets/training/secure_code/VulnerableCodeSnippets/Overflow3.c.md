# Question
 
What is the problem here?
 
```
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
       char *ptr_h;
       char h[64];
       ptr_h = getenv("HOME");
       if(ptr_h != NULL) {
               sprintf(h, "Your home directory is: %s !", ptr_h);
               printf("%s\n", h);
       }
       return 0;
}
```
 
-----SPLIT-----
 
# Answer

It is an Buffer Overflow issue. The code gets "HOME" enviroment value and copies it to a buffer, which has only 64 chars limit. No size control takes place and anything more than that limit causes the issue. https://owasp.org/www-community/attacks/Buffer_Overflow_via_Environment_Variables
