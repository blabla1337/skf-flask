# Question
 
What is the problem here?
 
```
int writeDataFromSocketToFile(char *host, int port)
{
	char filename[FILENAME_SIZE];
	char buffer[BUFFER_SIZE];
	int socket = openSocketConnection(host, port);

	if (socket < 0) {
		printf("Unable to open socket connection");
		return(FAIL);
	}
	if (getNextMessage(socket, filename, FILENAME_SIZE) > 0) {
		if (openFileToWrite(filename) > 0) {
			while (getNextMessage(socket, buffer, BUFFER_SIZE) > 0){
				if (!(writeToFile(buffer) > 0))
					break;
			}
		}
		closeFile();
	}
	closeSocket(socket);
}
```
 
-----SPLIT-----
 
# Answer

It is a Denial of Service issue. In the following example a server socket connection is used to accept a request to store data on the local file system using a specified filename. The method openSocketConnection establishes a server socket to accept requests from a client. When a client establishes a connection to this service the getNextMessage method is first used to retrieve from the socket the name of the file to store the data, the openFileToWrite method will validate the filename and open a file to write to on the local file system. The getNextMessage is then used within a while loop to continuously read data from the socket and output the data to the file until there is no longer any data from the socket. This example creates a situation where data can be dumped to a file on the local file system without any limits on the size of the file. This could potentially exhaust file or disk resources and/or limit other clients' ability to access the service. https://cwe.mitre.org/data/definitions/400.html