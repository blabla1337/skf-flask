import json
with open("desc_sol.json",encoding='utf-8') as read_file:
        data = json.load(read_file)

a=data['items']

title=[]

for d in a:
	title.append((d['title']))

file=open("entity_title.txt","x")
for i in title:
	file.write(i+"\n")
file.close()


