# White listing
-------

## Example:

    
    def check_pattern(param, list = [])
      // List should be an array of allowed patterns
      // list = ["value1", "value2"]
      if list.include? param
        Rails.logger.info "//{session.id} -> Good whitelist validation"
        true
      else
        Rails.logger.warn "//{session.id} -> Bad whitelist validation"
        false
      end
    end
