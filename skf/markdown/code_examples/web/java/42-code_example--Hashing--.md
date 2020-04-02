# Hashing
-------

## Example:


	package com.Lib;

	import java.io.UnsupportedEncodingException;
	import java.security.InvalidKeyException;
	import java.security.NoSuchAlgorithmException;
	import java.security.SecureRandom;
	import org.apache.commons.codec.binary.Base64;
	import org.apache.log4j.Logger;

	public class Hashing {

		final static Logger logger = Logger.getLogger(Hashing.class);
		
		public String createSalt(String password) throws NoSuchAlgorithmException, InvalidKeyException, UnsupportedEncodingException
		{
			/*
			For generating the random salt we want to use a secure cryptographic function
			*/
			
			SecureRandom sr = SecureRandom.getInstance("SHA1PRNG");
			//Create array for salt
			byte[] salt = new byte[128];
			//Get a random salt
			sr.nextBytes(salt);
			//return salt		
			
			/**
			* RFC 2898 password derivation compatible with .NET Rfc2898DeriveBytes class.
			*/
			Rfc2898DeriveBytes hasher = new Rfc2898DeriveBytes(password, salt, 10000);
			String bencoded = new String(Base64.encodeBase64(hasher.GetBytes(25)));
			return bencoded;	
		}
		
		//The salt in this function is the return value of the createSalt function
		public String hashPassword(String Salt, String Password)
		{
			Rfc2898DeriveBytes Hasher = null;
			try {
				Hasher = new Rfc2898DeriveBytes(Password + "ALongPepperValue",Salt.getBytes(), 10000);
			} catch (InvalidKeyException | NoSuchAlgorithmException | UnsupportedEncodingException e) {
				logger.error("error in hashing password!" + e.toString());
			}
			String bencoded = new String(Base64.encodeBase64(Hasher.GetBytes(25)));
			return bencoded;
		}

		//With this function we validate the password hash
		public boolean Validate(String passwordHash, String saltHash, String enteredPassword)
		{
			Rfc2898DeriveBytes Hasher = null;
			try {
				Hasher = new Rfc2898DeriveBytes(enteredPassword + "ALongPepperValue",saltHash.getBytes(), 10000);
			} catch (InvalidKeyException | NoSuchAlgorithmException | UnsupportedEncodingException e) 
				logger.error("Validation error in hashing password!" + e.toString());
			}
			String bencoded = new String(Base64.encodeBase64(Hasher.GetBytes(25)));
			if (bencoded.equals(passwordHash))
				return true;
			return false;
		}
	}

