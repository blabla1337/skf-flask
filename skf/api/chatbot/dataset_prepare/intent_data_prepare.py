import json
import csv
with open("data.json",encoding='utf-8') as read_file:
        data = json.load(read_file)

a=data['items']
des=[]
title=[]
con=[]
for d in a:
	title.append((d['title']))
	
ques=[]
sol=[]
code=[]

text=open("title.txt","w")
for tx in title:
        text.write(tx+"\n")

for t in title:
	ques.append("What is "+ t + " ?")
	ques.append("What does "+ t + " mean ?")
	ques.append("Tell me something about "+ t + " ?")
	ques.append(t)
	ques.append("Explain " + t +" ?")
	ques.append("Elaborate " + t +" ?")
	ques.append("Can you tell me about " + t + " ?")
	ques.append("What do you know about " + t + " ?")
	ques.append("What can you tell me about " + t + " ?")
	ques.append("I want to know about XSS " + t )
	ques.append("Do you have information about " + t + " ?")

for t in title:
        sol.append("How to solve "+ t + " ?")
        sol.append("How to resolve "+ t + " ?")
        sol.append("How to mitigate "+ t + " ?")
        sol.append("Solution for "+ t)
        sol.append("Provide me some Solution for "+ t)
        sol.append("mitigation for "+ t)
        sol.append("How to stop "+ t + " ?")
        sol.append("How to defend "+ t + " ?")
        sol.append("How to get secured against "+ t + " ?")
        sol.append("Solution, "+t)

for t in title:
        code.append("Give me some sample code of "+ t )
        code.append("Code example of "+ t + " ?")
        code.append("Code of "+ t )
        


file=open("intent_data.csv","x")
file.write('class, question\n')
for x in ques:
		x=x.replace(",","")
		file.write('Description, '+x+"\n")	 
for y in sol:
		y=y.replace(",","")
		file.write('Solution, '+y+"\n")

for z in code:
		z=z.replace(",","")
		file.write('Code, '+z+"\n")

file.close()

