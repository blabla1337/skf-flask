## Description:

Hardware description language code incorrectly defines register defaults or hardware IP parameters to insecure values.

Integrated circuits and hardware IP software programmable controls and settings are commonly stored in register circuits. These register contents have to be initialized at hardware reset to defined default values that are hard coded in the hardware description language (HDL) code of the hardware unit. Hardware descriptive languages also support definition of parameter variables, which can be defined in code during instantiation of the hardware IP module. Such parameters are generally used to configure a specific instance of a hardware IP in the design. The system security settings of a hardware design can be affected by incorrectly defined default values or IP parameters. The hardware IP would be in an insecure state at power reset, and this can be exposed or exploited by untrusted software running on the system. Both register defaults and parameters are hardcoded values, which cannot be changed using software or firmware patches but must be changed in hardware silicon. Thus, such security issues are considerably more difficult to address later in the lifecycle. Hardware designs can have a large number of such parameters and register defaults settings, and it is important to have design tool support to check these settings in an automated way and be able to identify which settings are security sensitive.

## Mitigation:


PHASE:Architecture and Design:
During hardware design all the system parameters and register defaults must be reviewed to identify security sensitive settings

PHASE:Implementation:
The default values of these security sensitive settings need to be defined as part of the design review phase.

PHASE:Testing:
Testing phase should use automated tools to test that values are configured per design specifications.

