# Question
 
What is the problem here?
 
```
static void Main(string[] args){
    Console.WriteLine("Please enter an user name to verify");
    string userName = Console.ReadLine();
    DirectoryEntry de = new DirectoryEntry("LDAP://DC=mysecurecompany,DC=com");
    DirectorySearcher searcher = new DirectorySearcher(de);
    searcher.Filter = "(&(objectClass=user)(|(cn=" + userName + ")(sAMAccountName=" + userName + ")))"; 
    SearchResult results = searcher.FindAll();
    if (results != null){
        foreach (SearchResult result in results){
            foreach (string propName in result.Properties.PropertyNames){
                foreach (object myCollection in result.Properties[propName]){
                    Console.WriteLine(propName + " : " + myCollection.ToString());
                }
            }
        }
    }
    else{Console.WriteLine("User does not exist!");}
}
```
 
-----SPLIT-----
 
# Answer

It is an LDAP Injection issue. 'userName' parameter is not being checked for any malicious LDAP chars and used in query directly. The attacker can inject LDAP chars for exploitation.
