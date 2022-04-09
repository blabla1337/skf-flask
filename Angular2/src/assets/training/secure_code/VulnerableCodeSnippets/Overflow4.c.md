# Question
 
What is the problem here?
 
```
void host_lookup(char *user_supplied_addr){
	struct hostent *hp;
	in_addr_t *addr;
	char hostname[64];
	in_addr_t inet_addr(const char *cp);
	validate_addr_form(user_supplied_addr);
	addr = inet_addr(user_supplied_addr);
	hp = gethostbyaddr( addr, sizeof(struct in_addr), AF_INET);
	strcpy(hostname, hp->h_name);
}
```
 
-----SPLIT-----
 
# Answer

It is an Buffer Overflow issue. This example takes an IP address from a user, verifies that it is well formed and then looks up the hostname and copies it into a buffer. This function allocates a buffer of 64 bytes to store the hostname, however there is no guarantee that the hostname will not be larger than 64 bytes. If an attacker specifies an address which resolves to a very large hostname, then the function may overwrite sensitive data or even relinquish control flow to the attacker. https://cwe.mitre.org/data/definitions/121.html