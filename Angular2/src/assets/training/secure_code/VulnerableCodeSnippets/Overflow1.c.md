# Question
 
What is the problem here?
 
```
#include <stdio.h>
int main(int argc, char **argv)
{
	char buf[8];
	gets(buf);
	printf("%s\n", buf);
	return 0;
}
```
 
-----SPLIT-----
 
# Answer

It is an Buffer Overflow issue. The code reads an input and copies it to a buffer, which has only 8 chars limit. However, there is no size control for user input and anything more than 8 chars causes the issue. https://owasp.org/www-community/attacks/Buffer_overflow_attack