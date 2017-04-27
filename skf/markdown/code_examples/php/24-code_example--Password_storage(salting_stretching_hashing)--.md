
Password storage(salting/stretching/hashing)
-------

**Example:**

    <?php

    class passwordHash
    {

        private $defaultOptions = [
            'cost' => 12,
        ];

        public function createHash($pwd)
        {
            /*
            For the hashing of passwords we use php's default password hashing method (currently this is the same as
            PASSWORD_BCRYPT).
            */

            // Here we generate a hash
            return password_hash($pwd, PASSWORD_DEFAULT, $this->defaultOptions);
        }

        // Validate your password
        public function validatePassword($correctHash, $password)
        {
            if (password_verify($password, $correctHash)) {
                //After successful validation we want to log that password was validated successfully:
                setLog(
                    $_SESSION['userID'],
                    "Password return true",
                    "SUCCESS",
                    date('d-m-Y'),
                    $privelige,
                    "NULL"
                );

                // check if we need to rehash the current password because the hashing algorithm or cost could be updated
                if (password_needs_rehash($correctHash, PASSWORD_DEFAULT, $this->defaultOptions)) {
                    $newHash = $this->createHash($password);

                    // store it or something...
                }

                return true;
            } else {
                //We log invalid password use
                setLog($_SESSION['userID'], "Password return false", "FAIL", date('d-m-Y'), $privelige, "LOW");

                return false;
            }
        }
    }

    ?>



	
