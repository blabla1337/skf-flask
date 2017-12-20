# System commands

# Define the whitelist pattern and validation type andz input parameter like:
# get_files("value1,value2,etc", "alphanumeric", params['filename'], "3")
class SystemCommands
  # Ruby implementation of PHP escapeshellcmd written by Prof. Edgar Gonzalez
  def escape_shell_command(cmd)
    cmd.gsub(/(["'#&;`|*?~<>^()\[\]{}$\\\x0A\xFF])/) { '' }
  end

  # Whenever a system command is finished, you should properly sanitize and escape this user input.
  # System command methods examples are: %x{command}, `command`, system("command")

  # First, we want to filter the filenames for expected values. For this example we use only az/09
  # Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
  # for more information about validation see "input validations" in the code examples:
  def exec(param, validation_type, pattern)
    validator = Validation.new

    case validation_type
    when numeric
      return false unless validator.numeric?(command)
    when alphanumeric
      return false unless validator.alphanumeric?(command)
    else
      return false
    end

    return false unless check_pattern(param, pattern)

    # If all went good we include the filename
    # Even though there is a match we still escape the shellcommand:
    command = './configure ' + param
    escaped_command = self.escape_shell_command(command)

    # Only after validation do we put the shell command into the system() method:
    system(escaped_command)
  end
end
