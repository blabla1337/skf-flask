# Question
 
What is the problem here?
 
```
char *lccopy(const char *str) {
  char buf[64];
  char *p;

  strcpy(buf, str);
  for (p = buf; *p; p++) {
    if (isupper(*p)) {
      *p = tolower(*p);
    }
  }
  return strdup(buf);
}
```
 
-----SPLIT-----
 
# Answer

It is an Buffer Overflow issue. The function takes a string as its argument and returns a heap-allocated copy of the string with all uppercase letters converted to lowercase. However, no size control takes place and anything more than 64 chars size causes the issue. https://owasp.org/www-community/vulnerabilities/Buffer_Overflow