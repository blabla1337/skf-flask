# Question
 
What is the problem here?
 
```
int i;
unsigned int numWidgets;
Widget **WidgetList;

numWidgets = GetUntrustedSizeValue();
if ((numWidgets == 0) || (numWidgets > MAX_NUM_WIDGETS)) {
	ExitError("Incorrect number of widgets requested!");
	}
WidgetList = (Widget **)malloc(numWidgets * sizeof(Widget *));
printf("WidgetList ptr=%p\n", WidgetList);
for(i=0; i<numWidgets; i++) {
	WidgetList[i] = InitializeWidget();
	}
WidgetList[numWidgets] = NULL;
showWidgets(WidgetList);
```
 
-----SPLIT-----
 
# Answer

It is a Memory Corruption issue. The code allocates memory for a maximum number of widgets. It then gets a user-specified number of widgets, making sure that the user does not request too many. It then initializes the elements of the array using InitializeWidget(). Because the number of widgets can vary for each request, the code inserts a NULL pointer to signify the location of the last widget. However, this code contains an off-by-one calculation error (CWE-193). It allocates exactly enough space to contain the specified number of widgets, but it does not include the space for the NULL pointer. As a result, the allocated buffer is smaller than it is supposed to be (CWE-131). So if the user ever requests MAX_NUM_WIDGETS, there is an out-of-bounds write (CWE-787) when the NULL is assigned. Depending on the environment and compilation settings, this could cause memory corruption. https://cwe.mitre.org/data/definitions/787.html