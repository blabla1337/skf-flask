# Question
 
What is the problem here?
 
```
#!/usr/bin/ruby
puts "Pleases supply 2 numbers for calculation"
num1  = ARGV[0]
num2 = ARGV[1]
print "Numbers: " , num1 + " + " + num2 , " = "
print eval(num1 + " + " + num2)
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. Arguments are vulnerable to OS command injection attacks. An intruder can supply 'ruby commandExec.rb 10 20; id' as an input to run consecutive commands.