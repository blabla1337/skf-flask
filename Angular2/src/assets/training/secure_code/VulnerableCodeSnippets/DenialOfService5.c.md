# Question
 
What is the problem here?
 
```
int processMessagesFromServer(char *hostaddr, int port) {
	...
	int servsock;
	int connected;
	struct sockaddr_in servaddr;

	// create socket to connect to server
	servsock = socket( AF_INET, SOCK_STREAM, 0);
	memset( &servaddr, 0, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(port);
	servaddr.sin_addr.s_addr = inet_addr(hostaddr);

	do {
		// establish connection to server
		connected = connect(servsock, (struct sockaddr *)&servaddr, sizeof(servaddr));

		// if connected then read and process messages from server
		if (connected > -1) {

		// read and process messages
		...
		}

	// keep trying to establish connection to the server
	} while (connected < 0);

	// close socket and return success or failure
	...
}
```
 
-----SPLIT-----
 
# Answer

It is a Denial of Service issue. In the code the method processMessagesFromServer attempts to establish a connection to a server and read and process messages from the server. The method uses a do/while loop to continue trying to establish the connection to the server when an attempt fails. However, this will create an infinite loop if the server does not respond. This infinite loop will consume system resources and can be used to create a denial of service attack. To resolve this a counter should be used to limit the number of attempts to establish a connection. https://cwe.mitre.org/data/definitions/835.html