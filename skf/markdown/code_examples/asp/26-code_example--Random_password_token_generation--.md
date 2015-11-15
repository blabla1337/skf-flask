Random password/token generation
-------

**Example:**


	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Security.Cryptography;

	namespace MvcApplication1.Controllers
	{
		public class randomizer
		{
			public string generate(int numberOfBytes)
			{
				/*
				For generating the password we want to use a secure cryptographic function
				*/
				RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();

				//Then set the size of the password
				byte[] buffer = new byte[numberOfBytes];

				rng.GetBytes(buffer);

				//Then we base64 encode the string in order to prevent null bytes
				string randomString = System.Convert.ToBase64String(buffer);

				return randomString;
			}
		}
	}

	
