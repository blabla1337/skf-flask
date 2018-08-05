import json
with open("code_data.json",encoding='utf-8') as read_file:
        data = json.load(read_file)

a=data['items']

title=[]

for d in a:
	title.append((d['title']))

file=open("code_title.txt","x")
for i in title:
	file.write(i+"\n")
file.close()


