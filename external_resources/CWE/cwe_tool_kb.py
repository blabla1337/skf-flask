import csv
import re
with open("1000.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:


        split1 = re.sub('::', '\n\n', row["Potential Mitigations"], flags=re.DOTALL)
        split2 = re.sub(':DESCRIPTION:', ':\r\n', split1, flags=re.DOTALL)
        split3 = re.sub('nan', '', split2, flags=re.DOTALL)
        print(split3)
        print("")
        print("////////////////////////////////////////////")
        name = re.sub(' ', '_', row["Name"], flags=re.DOTALL)
        name = re.sub('-', '_', name, flags=re.DOTALL)
        name = re.sub('/', '_', name, flags=re.DOTALL)
        name = re.sub("[(]", '', name, flags=re.DOTALL)
        name = re.sub("'", '', name, flags=re.DOTALL)
        name = re.sub("[)]", '', name, flags=re.DOTALL)

        description = re.sub('nan', '', row["Extended Description"], flags=re.DOTALL)

        cwe = row["CWE-ID"]
        f=open(cwe+"-knowledge_base--"+name+"--.md","w+")
        for i in range(1):
            f.write("##Description:\r\n\r\n")
            f.write("%s\r\n\r\n" % (row["Description"]))
            f.write("%s\r\n\r\n" % (description))

            f.write("##Mitigation:\r\n")
            f.write("%s" % (split3))
        f.close()   
