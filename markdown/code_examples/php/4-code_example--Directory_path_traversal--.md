
Directory/path traversal
-------

**Example:**



		     
        //Check for path traversal patterns
        $array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
        
        foreach($array as $injectPattern)
        {
            while(preg_match($injectPattern , $_GET['userinput']]))
            {
                header('location:/login');
                die;
            }        
        }
        

        //also before inserting user input we also could make a whitelisting of allowed values
        
        $array = array("/page1/" ,"/page2/" ,"/etc/" ,"/etc/");
        
        foreach($array as $injectPattern)
        {
            while(!preg_match($injectPattern , $_GET['userinput']]))
            {
                header('location:/login');
                die;
            }        
        }
        

        //ready for include
        include($_GET['userinput']);



	