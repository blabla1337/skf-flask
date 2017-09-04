# RFC 2898 password derivation compatible with .NET Rfc2898DeriveBytes
-------

## Example:


package com.edw;

import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/*
 - RFC 2898 password derivation compatible with .NET Rfc2898DeriveBytes class.
*/

public final class Rfc2898DeriveBytes
{
	public static void main(String[] args) throws Exception
	{
		Rfc2898DeriveBytes rfc2898 = new Rfc2898DeriveBytes("*^@K#K@!        ", "*^@K#K@!".getBytes());

	}

	private Mac _hmacSha1;
	private byte[] _salt;
	private int _iterationCount;

	private byte[] _buffer = new byte[20];
	private int _bufferStartIndex = 0;
	private int _bufferEndIndex = 0;
	private int _block = 1;

	/**
	 * Creates new instance.
	 * 
	 * @param password
	 *            The password used to derive the key.
	 * @param salt
	 *            The key salt used to derive the key.
	 * @param iterations
	 *            The number of iterations for the operation.
	 * @throws NoSuchAlgorithmException
	 *             HmacSHA1 algorithm cannot be found.
	 * @throws InvalidKeyException
	 *             Salt must be 8 bytes or more. -or- Password cannot be null.
	 */
	public Rfc2898DeriveBytes(byte[] password, byte[] salt, int iterations) throws NoSuchAlgorithmException, InvalidKeyException
	{
		if ((salt == null) || (salt.length < 8))
		{
			throw new InvalidKeyException("Salt must be 8 bytes or more.");
		}
		if (password == null)
		{
			throw new InvalidKeyException("Password cannot be null.");
		}
		this._salt = salt;
		this._iterationCount = iterations;
		this._hmacSha1 = Mac.getInstance("HmacSHA1");
		this._hmacSha1.init(new SecretKeySpec(password, "HmacSHA1"));
	}

	/**
	 * Creates new instance.
	 * 
	 * @param password
	 *            The password used to derive the key.
	 * @param salt
	 *            The key salt used to derive the key.
	 * @param iterations
	 *            The number of iterations for the operation.
	 * @throws NoSuchAlgorithmException
	 *             HmacSHA1 algorithm cannot be found.
	 * @throws InvalidKeyException
	 *             Salt must be 8 bytes or more. -or- Password cannot be null.
	 * @throws UnsupportedEncodingException
	 *             UTF-8 encoding is not supported.
	 */
	public Rfc2898DeriveBytes(String password, byte[] salt, int iterations) throws InvalidKeyException, NoSuchAlgorithmException,
			UnsupportedEncodingException
	{
		this(password.getBytes("UTF8"), salt, iterations);
	}

	/**
	 * Creates new instance.
	 * 
	 * @param password
	 *            The password used to derive the key.
	 * @param salt
	 *            The key salt used to derive the key.
	 * @throws NoSuchAlgorithmException
	 *             HmacSHA1 algorithm cannot be found.
	 * @throws InvalidKeyException
	 *             Salt must be 8 bytes or more. -or- Password cannot be null.
	 * @throws UnsupportedEncodingException
	 *             UTF-8 encoding is not supported.
	 */
	public Rfc2898DeriveBytes(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeyException,
			UnsupportedEncodingException
	{
		this(password, salt, 0x3e8);
	}

	/**
	 * Returns a pseudo-random key from a password, salt and iteration count.
	 * 
	 * @param count
	 *            Number of bytes to return.
	 * @return Byte array.
	 */
	public byte[] GetBytes(int count)
	{
		byte[] result = new byte[count];
		int resultOffset = 0;
		int bufferCount = this._bufferEndIndex - this._bufferStartIndex;

		if (bufferCount > 0)
		{ // if there is some data in buffer
			if (count < bufferCount)
			{ // if there is enough data in buffer
				System.arraycopy(this._buffer, this._bufferStartIndex, result, 0, count);
				this._bufferStartIndex += count;
				return result;
			}
			System.arraycopy(this._buffer, this._bufferStartIndex, result, 0, bufferCount);
			this._bufferStartIndex = this._bufferEndIndex = 0;
			resultOffset += bufferCount;
		}

		while (resultOffset < count)
		{
			int needCount = count - resultOffset;
			this._buffer = this.func();
			if (needCount > 20)
			{ // we one (or more) additional passes
				System.arraycopy(this._buffer, 0, result, resultOffset, 20);
				resultOffset += 20;
			}
			else
			{
				System.arraycopy(this._buffer, 0, result, resultOffset, needCount);
				this._bufferStartIndex = needCount;
				this._bufferEndIndex = 20;
				return result;
			}
		}
		return result;
	}

	private byte[] func()
	{
		this._hmacSha1.update(this._salt, 0, this._salt.length);
		byte[] tempHash = this._hmacSha1.doFinal(getBytesFromInt(this._block));

		this._hmacSha1.reset();
		byte[] finalHash = tempHash;
		for (int i = 2; i <= this._iterationCount; i++)
		{
			tempHash = this._hmacSha1.doFinal(tempHash);
			for (int j = 0; j < 20; j++)
			{
				finalHash[j] = (byte) (finalHash[j] ^ tempHash[j]);
			}
		}
		if (this._block == 2147483647)
		{
			this._block = -2147483648;
		}
		else
		{
			this._block += 1;
		}

		return finalHash;
	}

	private static byte[] getBytesFromInt(int i)
	{
		return new byte[] { (byte) (i >>> 24), (byte) (i >>> 16), (byte) (i >>> 8), (byte) i };
	}

}

