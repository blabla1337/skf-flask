# Identifier based authorization
-------

## Example:


    def identifier_based_authorization(input_parameter, pattern, id_to_auth)
      validator = Validation.new

      // First, we want to filter the filenames for expected values. For this example we use only numeric
      // Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
      // for more information about validation see "input validations" in the code examples:
      return false unless validator.numeric?(input_parameter)

      // Second, we want to whitelist the filenames for expected values, in this example they are,
      // file1,file2 etc.. for more information about whitelisting see "whitelisting" in the code examples:
      // pass the pattern to the check pattern, for instance  pattern = %w[file1 file2]
      return false unless check_pattern(input_parameter, pattern)

      // Whenever you are checking whether a user is restricted to review certain data,
      // the access restrictions should be processed serverside.
      user = User.find_by(auth_id: input_parameter)

      return true if id_to_auth == user.auth_id

      false
    end
