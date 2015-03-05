
Password storage(salting/stretching/hashing)
-------

**Example:**

    <?php

    /*
    For the encryption of passwords we use php's BCRYPT encryption method.
    */

    //Here we generate a hash with a random salt
    function HashPassword($password){
        $options = [
        'cost' => 11,
        'salt' => mcrypt_create_iv(22, MCRYPT_DEV_URANDOM),
        ];

        $hash =	password_hash($password, PASSWORD_BCRYPT, $options)."\n";

        return $hash;
        }

        //Validates a password
        //returns true if match correct
    function ValidatePassword($correctHash, $password)
    {

        if (password_verify($password, $correctHash))
        {
            return true;
        }

    }

    ?>



	
