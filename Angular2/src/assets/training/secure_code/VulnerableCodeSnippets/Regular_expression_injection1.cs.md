# Question
 
What is the problem here?
 
```
static void Main(string[] args){
    Console.WriteLine("Please enter your account id:");
    string accountID = Console.ReadLine();
    Console.WriteLine("Please enter your account name:");
    string accountName = Console.ReadLine();

    Regex regex = new Regex(accountID);
    Match match = regex.Match("^.*"+ accountName + ".*$");

    if (match.Success)
        Console.WriteLine("Account info is matched");
    else
        Console.WriteLine("Records do not match!");
}
```
 
-----SPLIT-----
 
# Answer

It is an Regular Expression Injection issue. User supplied parameter is being used to create regular expression and the attacker has full control over query criteria.