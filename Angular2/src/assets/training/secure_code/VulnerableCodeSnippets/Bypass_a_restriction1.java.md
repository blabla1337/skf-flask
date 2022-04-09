# Question
 
What is the problem here?
 
```
while(true) {
	DatagramPacket rp=new DatagramPacket(rData,rData.length);
	outSock.receive(rp);
	String in = new String(p.getData(),0, rp.getLength());
	InetAddress clientIPAddress = rp.getAddress();
	int port = rp.getPort();
	if (isTrustedAddress(clientIPAddress) & secretKey.equals(in)) {
		out = secret.getBytes();
		DatagramPacket sp =new DatagramPacket(out,out.length, IPAddress, port); outSock.send(sp);
	}
}
```

-----SPLIT-----
 
# Answer

It is a Bypassing Restriction issue. The code checks if a request is from a trusted address before responding to the request. However it only verifies the address as stored in the request packet. An attacker can spoof this address, thus impersonating a trusted client. https://cwe.mitre.org/data/definitions/290.html