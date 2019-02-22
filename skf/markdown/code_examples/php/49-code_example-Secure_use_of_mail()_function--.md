# Secure use of mail() function
-------

## Example:

    /*
    PHP comes with the built-in function mail() for sending emails from a PHP application. The mail delivery can be configured by using the following five parameters.

    http://php.net/manual/en/function.mail.php

    bool mail(	
        string $to, 
        string $subject,
        string $message [, 
        string $additional_headers [, 
        string $additional_parameters ]]
    )
    In order to use the mail() function in PHP, an email program or server has to be configured. The following two options can be used in the php.ini configuration file:

    1)Configure an SMTP server’s hostname and port to which PHP connects
    2)Configure the file path of a mail program that PHP uses as a Mail Transfer Agent (MTA)

    When PHP is configured with the second option, calls to the mail() function will result in the execution of the configured MTA program. Although PHP internally applies escapeshellcmd() to the program call which prevents an injection of new shell commands, the 5th argument $additional_parameters in mail() allows the addition of new program arguments to the MTA. Thus, an attacker can append program flags which in some MTA’s enables the creation of a file with user-controlled content.
    */

   	<?php

        /* 
        It is important that user input should not be passed into the fifth parameter of the mail() function.

        Since first 4 parameters can get added to logs, it is important that they should not contain  any php code

        !preg_match( "/[\r\n]/", $additional_parameters ) is used to mitigate any header injection attack

        Below code is implemented considering all 5 parameters are user controllable
        */

       if(!strpos($to, '<?') && !strpos($subject, '<?') && !strpos($message, '<?') && !strpos($additional_headers, '<?') && !strpos($additional_parameters, '<?') && !preg_match( "/[\r\n]/", $additional_parameters )){

           /*
           A PHP function is used to escape command-line arguments, which replaces escapeshellarg with more robust methods for both Windows and non-Windows platforms. 
           Install it from https://packagist.org/packages/winbox/args
           */

           mail(Winbox\Args::escape($to), Winbox\Args::escape($subject), Winbox\Args::escape($message), Winbox\Args::escape($additional_headers), Winbox\Args::escape($additional_options));

       }

       /*
        If fifth parameter is user controllable this implementation does not stop an attacker to append program flags which in some MTA’s enables the read and creation of a file.
        
        Hence additional checks should be implemented for the type of input expected in fifthe parameter
        */

    ?>