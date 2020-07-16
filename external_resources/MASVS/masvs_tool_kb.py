import json
import re

with open('masvs.json') as json_file:
    data = json.load(json_file)
    for p in data[0]:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

        #split1 = re.sub('::', '\n\n', row["Potential Mitigations"], flags=re.DOTALL)
        #description = re.sub('nan', '', row["Extended Description"], flags=re.DOTALL)
        #cwe = row["CWE-ID"]
        
        #f=open(cwe+"-knowledge_base--"+name+"--.md","w+")
        #for i in range(1):
        #    f.write("## Description:\r\n\r\n")
        #    f.write("%s\r\n\r\n" % (row["Description"]))
        #    f.write("%s\r\n\r\n" % (description))
        #    f.write("## Mitigation:\r\n")
        #    f.write("%s" % (split3))
        #f.close()   
