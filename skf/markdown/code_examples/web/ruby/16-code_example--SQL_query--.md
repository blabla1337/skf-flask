# SQL Query
-------

## Example:

    
    // You should try to use Active Record's prepared methods to handle SQL Queries.
    // Example 1: Take client with id = 40 from the database
    client = Client.find(40)

    // Example 2: Take last 5 clients
    client = Client.last(5)

    // Example 3: Find client by first name
    client = Client.find_by first_name: "Wojciech"

    // Example 4: Where conditions
    // With 1 parameter
    Client.where("parameter = ?", params[:parameter]) 
    Client.where("parameter1 = ? AND parameter2 = ?", params[:parameter1], params[:parameter2])

    // !!!!!
    // Using SQL Queries like this Client.where("param1 LIKE '%//{params[:param1]}%'")
    // leads to SQL Injection attack. Never do that!
    // !!!!!


    // Example 5: Range conditions
    Client.where(created_at: (Time.now.midnight - 1.day)..Time.now.midnight)

    // For more methods and examples check http://guides.rubyonrails.org/active_record_querying.html

