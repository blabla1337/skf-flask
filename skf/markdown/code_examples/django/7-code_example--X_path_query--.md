# X-path query
-------

## Example:

    
    """
    Define the allowed characters and input parameter and count level for the
    user lockout like:
    controller("<'>&", $_GET['filename'], "3")
    
    In order to prevent x-path injections we have to treat these query's similar as 
    to the sql query's. 
    """
    
    def controller(allowed, input, count):
        
        """
        First we build our encoding method, see "input validation" code example for
        more detailed information about encoding and escaping.
        """
        
        return = encoder(allowed, input, count)

        //If the encoder came back false we do not process the function!
        if return != False:

            //Parse the register.xml
            root = etree.parse("register.xml")
            //Extract the id from the XML using XPath
            find = etree.XPath('/Employees/Employee[ID=' + return + ']')

            for x in find(root):
                print x.text
