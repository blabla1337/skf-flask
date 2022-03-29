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

It is an Race Condition issue. The report should be only executed on Mondays, however after the 'if' control, there is nothing more control takes place. You can run the app Monday to pass this 'if' statement and then you can generate reports any day you want.
