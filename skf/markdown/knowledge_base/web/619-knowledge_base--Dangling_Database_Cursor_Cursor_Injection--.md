## Description:

If a database cursor is not closed properly, then it could become accessible to other users while retaining the same privileges that were originally assigned, leaving the cursor dangling.

For example, an improper dangling cursor could arise from unhandled exceptions. The impact of the issue depends on the cursor's role, but SQL injection attacks are commonly possible.

## Mitigation:


PHASE:Implementation:
Close cursors immediately after access to them is complete. Ensure that you close cursors if exceptions occur.

