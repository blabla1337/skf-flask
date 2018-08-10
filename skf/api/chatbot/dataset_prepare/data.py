import requests
import json
def extract_from_api():
	r_kb = requests.get("https://demo.securityknowledgeframework.org/api/kb/items", verify = False)
	r_code = requests.get("https://demo.securityknowledgeframework.org/api/code/items", verify = False)

	f_kb = open(os.path.join(app.root_path, "api/chatbot/datasets/data.json",'w'))
	f_code = open(os.path.join(app.root_path, "api/chatbot/datasets/code_data.json", "w"))

	f_kb.write(r_kb.content.decode('utf-8'))
	f_code.write(r_code.content.decode('utf-8'))

	f_kb.close()
	f_code.close()


def desc_sol_data():
	with open(os.path.join(app.root_path, "api/chatbot/datasets/data.json",encoding='utf-8')) as read_file:
        	data = json.load(read_file)

	file_des_sol=open(os.path.join(app.root_path, "api/chatbot/datasets/desc_solution.json","w"))
	file_des_sol.write("{\n"+'"items": [\n')
	a=data['items']
	for i in range(len(a)):
		file_des_sol.write("{\n")
		file_des_sol.write('"kbId": '+str(a[i]['kbID'])+",\n")
		file_des_sol.write('"title": "'+ a[i]['title']+'",\n')
		y=a[i]['content']
		y=y.replace("\n\n","")
		y=y.replace("\n\n\n","")
		y=y.replace("\n"," ")
		y=y.split("Solution:")
		y[0]=y[0].split("Description:")
		file_des_sol.write('"Description": '+json.dumps(y[0][1])+",\n")
		if (i+1)<len(a):
			file_des_sol.write('"Solution": '+json.dumps(y[1])+"\n},\n")
		else:
			file_des_sol.write('"Solution": '+json.dumps(y[1])+"} ")
	file_des_sol.write("]"+"\n"+"}")
	file_des_sol.close()

def entity_data():
	with open(os.path.join(app.root_path, "api/chatbot/datasets/data.json",encoding='utf-8')) as read_file:
	        data = json.load(read_file)

	a=data['items']

	title=[]

	for d in a:
		title.append((d['title']))

	file_entity=open(os.path.join(app.root_path, "api/chatbot/datasets/entity_title.txt","w"))
	for i in title:
		file_entity.write(i+"\n")
	file_entity.close()

def intent_data():
	with open(os.path.join(app.root_path, "api/chatbot/datasets/data.json",encoding='utf-8')) as read_file:
	        data = json.load(read_file)

	a=data['items']
	title=[]
	for d in a:
		title.append((d['title']))
	ques=[]
	sol=[]
	code=[]
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


	file=open(os.path.join(app.root_path, "api/chatbot/datasets/intent_data.csv","w"))
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

def code_entity():
	with open(os.path.join(app.root_path, "api/chatbot/datasets/code_data.json",encoding='utf-8')) as read_file:
	        data = json.load(read_file)

	a=data['items']

	title=[]

	for d in a:
		title.append((d['title']))

	file_code=open(os.path.join(app.root_path, "api/chatbot/datasets/code_title.txt","w"))
	for i in title:
		file_code.write(i+"\n")
	file_code.close()


#extract_from_api()
#desc_sol_data()
#entity_data()
#intent_data()
#code_entity()
