TLS certificate public key pinning
-------

**Description:**

Pinning is the process of associating a host with their expected X509 certificate or 
public key. Once a certificate or public key is known or seen for a host, the certificate 
or public key is associated or 'pinned' to the host. If more than one certificate or 
public key is acceptable, then the program holds a pinset 
(taking from Jon Larimer and Kenny Root Google I/O talk). In this case, the advertised 
identity must match one of the elements in the pinset.

**Solution:**

The idea is to re-use the existing protocols and infrastructure, but use them in a 
hardened manner. For re-use, a program would keep doing the things it used to do when 
establishing a secure connection.

To harden the channel, the program would take advantage of the OnConnect callback offered 
by a library, framework or platform. In the callback, the program would verify the 
remote host's identity by validating its certificate or public key. While pinning does
not have to occur in an OnConnect callback, its often most convenient because the 
underlying connection information is readily available. 

For more extended information on different types of implementation please see:
https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning




   
