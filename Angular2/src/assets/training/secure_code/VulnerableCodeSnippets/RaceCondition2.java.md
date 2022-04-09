# Question
 
What is the problem here?
 
```
public static void main(String []args){
    Calendar today = Calendar.getInstance();
    if (today.get(Calendar.DAY_OF_WEEK) == Calendar.FRIDAY) {
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
        System.out.println("Reports can be only generated on Fridays");
    }
}
```
 
-----SPLIT-----
 
# Answer

It is a Race Condition issue. The report should be only executed on Fridays, however after the 'if' control, there is nothing more control takes place. Once you pass this 'if' statement and then you can generate reports any day you want. So you should run the application on Fridays and provide inputs when you want to execute the task.
