# Question
 
What is the problem here?
 
```
public static void main(String []args){
    System.out.println("Wellcome to backup service!");
    System.out.println("How often you want to take root folder's full backup? 24hours / ?");
    int howManyBackupsPerDay = Integer.parseInt(System.console().readLine());
    int _minute =(int) Math.ceil(24 *60 / (float)howManyBackupsPerDay);
    System.out.println("It will be perfromed once in " + _minute + " minute");
    while (true) {
    try {
        performFullBackup();
        Thread.sleep(_minute);
        } 
    catch(InterruptedException ex) {
        Thread.currentThread().interrupt();
        }
    }
}
public static void performFullBackup(){
    //backup process
}
```
 
-----SPLIT-----
 
# Answer

It is a Denial Of Service issue. There is no limit on user supplied value. Users can take as much as backups she/he wants and that causes both disk and system source issues. Backup process may keep CPU busy and fill the disk excessively.