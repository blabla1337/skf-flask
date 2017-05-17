Randomizer 
----------------

***Example:***


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



package com.edw;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import org.apache.log4j.Logger;

public class Randomizer {
	
	private List<Integer> bytes = new ArrayList<>();
    private int address = 0;
	final static Logger logger = Logger.getLogger(Randomizer.class);
	
	public String randomize()
	{		
		SecureRandom csprng = new SecureRandom();
		byte[] randomBytes = new byte[128];
		csprng.nextBytes(randomBytes);
		String csrftoken = Base64.getEncoder().encodeToString(randomBytes);
		
		return csrftoken;		
	}
	
	public String generateToken(int numberOfBytes)
	{		
		SecureRandom csprng = new SecureRandom();
		byte[] randomBytes = new byte[numberOfBytes];
		csprng.nextBytes(randomBytes);
		String csrftoken = null;
		try {
			csrftoken = this.bin2hex(randomBytes[0]);
		} catch (Exception e) {
			 logger.error("cannot write to file : "  + e.toString());
		}
		return csrftoken;		
	}
	public String generate(int numberOfBytes)
	{		
		SecureRandom csprng = new SecureRandom();
		byte[] randomBytes = new byte[numberOfBytes];
		csprng.nextBytes(randomBytes);
		String csrftoken = Base64.getEncoder().encodeToString(randomBytes);
		return csrftoken;		
	}
	
	public String secure_password(int numberOfBytes)
	{		
		SecureRandom csprng = new SecureRandom();
		byte[] randomBytes = new byte[numberOfBytes];
		csprng.nextBytes(randomBytes);
		String token = randomBytes.toString();
		return token;		
	}
	

    public void setAddress(int address) {
        this.address = address;
    }

    public String bin2hex(int byt) throws Exception {
    	if (bytes.size() == 0xFF) {
            throw new Exception("Too many bytes");        
            }
        bytes.add(byt);
        int sum = 0;
        StringBuilder sb = new StringBuilder();
        sb.append(':');
        sb.append(toHexString(bytes.size(), 2));
        sum += bytes.size();
        sb.append(toHexString(address, 4));
        sum += (address & 0xFF00) >> 8;
        sum += address & 0xFF;
        address += bytes.size();
        sb.append("00");
        for (Integer b : bytes) {
            sum += b;
            sb.append(toHexString(b, 2));
        }
        sb.append(toHexString((~(sum & 0xFF) + 1) & 0xFF, 2));
        bytes.clear();
        return sb.toString();
    }

    private String toHexString(int i, int len) {
        String hex = Long.toHexString(i).toUpperCase();
        if (len == 2) {
            if (hex.length() == 1) {
                return "0" + hex;
            } else {
                return hex;
            }
        } else {
            if (hex.length() == 1) {
                return "000" + hex;
            } else if (hex.length() == 2) {
                return "00" + hex;
            } else if (hex.length() == 3) {
                return "0" + hex;
            } else {
                return hex;
            }
        }
    }
}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~