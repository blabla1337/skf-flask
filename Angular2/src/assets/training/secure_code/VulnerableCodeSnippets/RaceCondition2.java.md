# Question
 
What is the problem here?
 
```
public static void main(String []args){
    Calendar today = Calendar.getInstance();
    if (today.get(Calendar.DAY_OF_WEEK) == Calendar.MONDAY) {
        System.out.println("You can generate the weekly report today. Please enter your email address to proceed");
        String emailAdd = System.console().readLine();
        String regex = "^(.+)@company.com";
        Pattern pattern = Pattern.compile(regex);
        if (pattern.matcher(emailAdd).matches()){
            System.out.println("The process is about to start, you will receive the report soon!");
            weeklyReportGenerator(emailAdd);
        }
        else {
            System.out.println("Please provide a valid company email address!");
        }
    }else {
        System.out.println("Reports can be only generated on Mondays");
    }
}
```
 
-----SPLIT-----
 
# Answer

It is an Race Condition issue. The report should only executed on Mondays, however after the 'if' control there is nothing more takes place. You can run the app Monday to pass this 'if' control and then you can generate reports any day you want.