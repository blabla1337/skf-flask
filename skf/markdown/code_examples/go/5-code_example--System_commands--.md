# System commands
-------

## Example:

	package main


	import (
		"fmt"
		"log"
		"os/exec"
		"regexp"
	)

	// Reference:
	// https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Injection_Prevention_Cheat_Sheet.md#operating-system-commands

	/*
		White list Regular Expression - where is explicitly defined a whitelist of good characters allowed and the maximum length of the string. Ensure that metacharacters like & | ; $ > < \ \ !` and white-spaces are not part of the Regular Expression. For example, the following regular expression only allows lowercase letters and numbers, and does not contain metacharacters. The length is also being limited to 3-10 characters:
		Ensure to not compile the regex inside your validation function.
	*/
	const dirWhitelist string = "^[a-z0-9]{3,10}$"
	var dirWhitelistRegex = regexp.MustCompile(dirWhitelist)
    
	func validateDirectory(dir string) bool {
			return dirWhitelistRegex.MatchString(dir)
	}

	func validateParameters(params []string) error {
		allowedParameters := map[string]string{
			"-l": "-l",
			"-a": "-a",
			"-h": "-h",
		}
		for _, p := range params {
			if _, ok := allowedParameters[p]; !ok {
				return fmt.Errorf("parameter %s not allowed", p)
			}
		}
		
		return nil
	}

	func main() {
		// If possible, prevent user entered input directly into command arguments.
		// If this is not feasible, use input validation on the values for commands and/or the relevant arguments.
		// Positive or “whitelist” input validation - where are the arguments allowed explicitly defined
		userSuppliedParameters := []string{"-l"}
		if err := validateParameters(userSuppliedParameters); err != nil {
			log.Fatalf("error validating user supplied parameters: %s", err.Error())
		}
		userSuppliedDir:= "validdir"
		if ok := validateDirectory(userSuppliedDir); !ok {
			log.Fatalf("error validating user supplied directory. must match %s", dirWhitelist)
		}
		
		// Command returns the Cmd struct to execute the named program with the given arguments.
		out, err := exec.Command("ls", "-lah", userSuppliedDir).Output()
		if err != nil {
			log.Fatalf("error running command: %s", err.Error())
		}
		fmt.Printf("command ran: %s\n", string(out))
	}