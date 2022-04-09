# Question
 
What is the problem here?
 
```
<?php
class UserCars
{
   private $hook;
   public $car_model;
   public $car_year;
   public $car_color;

   function __construct($car_model, $car_year, $car_color) {
    $this->car_model = $car_model;
    $this->car_year = $car_year;
    $this->car_color = $car_color;
   }

   function __wakeup()
   {
      if (isset($this->hook)) eval($this->hook);
   }

   function get_model() {
    return $this->car_model;
   }
   
   function get_year() {
    return $this->car_year;
   }

   function get_color() {
    return $this->car_color;
   }
}

$car_data = unserialize($_COOKIE['data']);
$cars = new UserCars("TOGG", "2023", "Blue");
echo $cars->get_model();
echo "<br>";
echo $cars->get_year();
echo "<br>";
echo $cars->get_color();
?>
```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. The example shows a PHP class with an exploitable 'wakeup' method. an attacker might be able to perform a Code Injection attack by sending an HTTP request like this: _'Cookie: data=O%3A8%3A%22Example2%22%3A1%3A%7Bs%3A14%3A%22%00Example2%00hook%22%3Bs%3A10%3A%22phpinfo%28%29%3B%22%3B%7D'_ - https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection
