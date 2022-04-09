# Question
 
What is the problem here?
 
```
public static void userFunc(){
	Console.WriteLine("Your commands will be executed with low privilege user and command output will be saved to your home folder.");
	int userID;
	Process process = new Process();
	try
	{	
		escalatePrivileges();
		Console.WriteLine("Please supply your userID for home folder creation:");
		userID =  Convert.ToInt32(Console.ReadLine());
		string homeFolder=@"C:\" + userID.ToString();
		createHomeFolder(homeFolder)
		Console.WriteLine("Your home folder has been created!");
		lowerPrivileges();
	}
	catch (Exception ex){}

    Console.WriteLine("What command you want to run:");
	String userCommand =  Console.ReadLine();
	userCommand = userCommand.Replace(";","").Replace("|","").Replace("||","").Replace("&","").Replace("&&","");
	process.StartInfo.FileName = userCommand;
    process.StartInfo.RedirectStandardOutput = true;
    process.Start();    
    string output = process.StandardOutput.ReadToEnd();
    Console.WriteLine(output);
    process.WaitForExit();
	using StreamWriter file = new(@"C:\"+ userID.ToString(), append: true);
    await file.WriteLineAsync(output);
}
```
 
-----SPLIT-----
 
# Answer

It is a Gain Privileges issue. The code escalates its own privilege to perform some tasks however this can be abused by end-users. According to the example, home folders are being created with 'escalatePrivileges' function, but if any exception occurs the application can not execute 'lowerPrivileges' and it keeps running with high-privilege role.
