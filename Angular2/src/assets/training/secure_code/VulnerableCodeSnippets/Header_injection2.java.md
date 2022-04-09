# Question
 
What is the problem here?
 
```
public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
	Part filePart = request.getPart("userFile");	
	String reqContentType = request.getContentType(); 	
	if (reqContentType.equals("application/pdf")){
	    InputStream fileInputStream = filePart.getInputStream();
	    File fileToSave = new File("tmp/" + filePart.getSubmittedFileName());
		Files.copy(fileInputStream, fileToSave.toPath());
		response.getOutputStream().println("<p>Your file has been uploaded</p>");
	}
	else{
		response.getOutputStream().println("<p>Only pdf files are supported!</p>");
	}
}
```
 
-----SPLIT-----
 
# Answer

It is a Header Injection issue. 'Content-Type' parameter is vulnerable for manipulation. Attacker can change the request 'content-type' to anything to upload files she/he wants. The application only allows pdf files, however the restriction can be easily bypassed.