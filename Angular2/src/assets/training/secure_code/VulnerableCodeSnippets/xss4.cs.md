# Question
 
What is the problem here?
 
```
[Route("/comments")]
public async void addComment(string userID, string userName, string userComment, DbContext context){
    var commentInsert = @"INSERT INTO comments (userID, userComment) VALUES (@userID, @userComment);";
    context.Database.ExecuteSqlCommand(commentInsert, new SqlParameter("@userID", userID), new SqlParameter("@userComment", userComment));
    var context = this.ControllerContext.HttpContext;
    await context.Response.WriteAsync("<body>Your comment is successfully added, thank you "+ userName +"</body>");
}
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'userName' parameter is vulnerable for injection attacks and no input sanitization exists. Injected javascript codes will be executed in the response. On the other hand, the database query looks fine.
