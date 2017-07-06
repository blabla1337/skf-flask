Password Storage (salting/stretching/hashing)
-------

**Example:**

	:::cs
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Security.Cryptography;

	namespace MvcApplication1.Controllers
	{
		public class hashing
		{
			public string createSalt(string password)
			{
				/*
				For generating the random salt we want to use a secure cryptographic function
				*/
				RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();

				//Then we generate a random salt
				byte[] buffer = new byte[128];
				rng.GetBytes(buffer);

				Rfc2898DeriveBytes hasher = new Rfc2898DeriveBytes(password + "ALongPepperValue", buffer, 10000);

				return Convert.ToBase64String(hasher.GetBytes(25));
			}
			
			//The salt in this function is the return value of the createSalt function
			public string hashPassword(string Salt, string Password)
			{
				Rfc2898DeriveBytes Hasher = new Rfc2898DeriveBytes(Password + "ALongPepperValue",
					System.Text.Encoding.Default.GetBytes(Salt), 10000);
				return Convert.ToBase64String(Hasher.GetBytes(25));
			}
			
			//With this function we validate the password hash
			public bool Validate(string passwordHash, string saltHash, string enteredPassword)
			{
				Rfc2898DeriveBytes Hasher = new Rfc2898DeriveBytes(enteredPassword + "ALongPepperValue",
						System.Text.Encoding.Default.GetBytes(saltHash), 10000);
				return Convert.ToBase64String(Hasher.GetBytes(25)) == passwordHash;
			}
		}
	}
