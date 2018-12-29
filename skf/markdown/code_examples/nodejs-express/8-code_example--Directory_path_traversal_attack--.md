# Directory Path traversal
-------

## Example:

    is_valid_path(path){
        /*
            First, we want to filter the filenames for expected values. For this example the filenames should consist of only alphanumeric characters which we validate with the following regexp
             /^[a-zA-Z0-9]+$/
        */
        valid = FILENAMES_REGEXP.test(filename)
        if(valid){
           return true
        }
        return false
     /* TODO: add logging */
      		
    }

    is_allowed_location(path){
        /*
            Then we whitelist the path to only the allowed locations using the path library.
            DIR_WHITELIST is an array of directory pathnames (such as /foo/bar/baz) the application is allowed to load resources from
        */
        if( DIR_WHITELIST.indexof(path.dirname(path)>-1){
            return true
        }
        return false
    }

    // the above methods could be used as follows
	app.get('/read_file', function(req, res) {
        filename = req.query.filename
        if(is_varlid_path(filename) and is_allowed_location(filename))
            serve_request()
        else{
            //return error
        }   

    })