## Description:

The product uses an automated mechanism such as machine learning to recognize complex data inputs (e.g. image or audio) as a particular concept or category, but it does not properly detect or handle inputs that have been modified or constructed in a way that causes the mechanism to detect a different, incorrect concept.

When techniques such as machine learning are used to automatically classify input streams, and those classifications are used for security-critical decisions, then any mistake in classification can introduce a vulnerability that allows attackers to cause the product to make the wrong security decision. If the automated mechanism is not developed or trained with enough input data, then attackers may be able to craft malicious input that intentionally triggers the incorrect classification. Targeted technologies include, but are not necessarily limited to: automated speech recognition automated image recognition For example, an attacker might modify road signs or road surface markings to trick autonomous vehicles into misreading the sign/marking and performing a dangerous action.

## Mitigation:
