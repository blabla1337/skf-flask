## Description:

Every Action Form must have a corresponding validation form.

If a Struts Action Form Mapping specifies a form, it must have a validation form defined under the Struts Validator.

## Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
Map every Action Form to a corresponding validation form. An action or a form may perform validation in other ways, but the Struts Validator provides an excellent way to verify that all input receives at least a basic level of validation. Without this approach, it is difficult, and often impossible, to establish with a high level of confidence that all input is validated.

