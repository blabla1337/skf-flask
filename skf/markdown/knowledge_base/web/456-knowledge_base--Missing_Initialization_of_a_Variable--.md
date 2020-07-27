##Description:

The software does not initialize critical variables, which causes the execution environment to use unexpected values.



##Mitigation:


PHASE:Implementation:
Check that critical variables are initialized.

PHASE:Testing:
Use a static analysis tool to spot non-initialized variables.

