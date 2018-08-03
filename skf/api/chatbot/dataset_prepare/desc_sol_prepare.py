import json
with open("data.json",encoding='utf-8') as read_file:
        data = json.load(read_file)

file=open("desc_solution.json","w")
file.write("{\n"+'"items": [\n')
a=data['items']
for i in range(len(a)):
	file.write("{\n")
	file.write('"kbId": '+str(a[i]['kbID'])+",\n")
	file.write('"title": "'+ a[i]['title']+'",\n')
	y=a[i]['content']
	y=y.replace("\n\n","")
	y=y.replace("\n\n\n","")
	y=y.replace("\n"," ")
	y=y.split("Solution:")
	y[0]=y[0].split("Description:")
	file.write('"Description": '+json.dumps(y[0][1])+",\n")
	if (i+1)<len(a):
		file.write('"Solution": '+json.dumps(y[1])+"\n},\n")
	else:
		file.write('"Solution": '+json.dumps(y[1])+"} ")
file.write("]"+"\n"+"}")

