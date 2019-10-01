Description:

user-supplied scriptable or expression template language content, such as Markdown, 
CSS or XSL stylesheets, BBCode, or similar are designed to give users the option
to add a lot of rich styling to the application. However whenever these templates 
do not filter for harmfull attacks, these templates can be used to leverage
XSS attacks.


Solution:

Verify that the application sanitizes, disables, or sandboxes 
user-supplied scriptable or expression template language content, such as Markdown, 
CSS or XSL stylesheets, BBCode, or similar.

How this is most effectively done depends on the framework and library you
are choosing to incorperate. It is advised to investigate how to put up constraints
for translating these template syntaxes to HTML tags and what their security
implications are. 
