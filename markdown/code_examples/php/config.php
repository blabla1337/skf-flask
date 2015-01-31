<?php


# Copyright 2014 Riccardo ten Cate



define ('DB_HOST',  'localhost');
define ('DB_NAME',  'skf');
define ('DB_USER',  'root');
define ('DB_PASS',  'root');


ini_set('session.cookie_httponly', 1);
ini_set('session.cookie_lifetime', 3600);
//ini_set('session.cookie_secure', 1);



// 
// Development done using Ubuntu 14 32bit
// apt-get install apache2 php5 php5-mcrypt php5-mysql php5-gd mysql-server 
// sudo php5enmod mcrypt && sudo a2enmod rewrite && sudo service apache2 restart
// set AllowOverride All in the /var/www/html virtual host config
//


//
//theme thanks to OnePage Design
//
//
