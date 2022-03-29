# Question
 
What is the problem here?
 
```
static void writefile(char *file2Process){
static FILE *localFile;
static struct stat statinfo;
if(file2Process != NULL){
	if((localFile = fopen(file2Process, "a")) == NULL)
		{
		fprintf(stdout, "error opening file %s: %s\n", file2Process, strerror(errno));
		return;
		}
	}
if(localFile != NULL) fclose(localFile);
if(stat(file2Process, &statinfo) == 0){
	if(statinfo.st_size == 0) remove(file2Process);
	}
return;
}
```
 
-----SPLIT-----
 
# Answer

It is a Race Condition issue. The code does not lock any system sources and performs 'if' statement, which is not reliable, because the criteria can be changed during the application run-time. Even it can be different before and after 'if' control.
