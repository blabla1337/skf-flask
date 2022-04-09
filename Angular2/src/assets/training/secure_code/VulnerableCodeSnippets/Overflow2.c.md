# Question
 
What is the problem here?
 
```
#include <stdio.h>
#include <string.h>

int main(void)
{
        printf("Please enter your username\n");
        char buf[16];
        gets(buf);
        if(strcmp(buff, "admin")){
                printf("Wellcome %s\n", buf);
        }
        else{
                printf ("\n Wrong Username \n");
        }
        return 0;
}
```
 
-----SPLIT-----
 
# Answer

It is an Buffer Overflow issue. The code reads an input and copies it to a buffer, which has only 16 chars limit. However, there is no size control for user input and anything more than this size causes the issue.