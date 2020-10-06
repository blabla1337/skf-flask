import re

# Using readlines() 
file1 = open('sql_raw.txt', 'r') 
Lines = file1.readlines() 

for line in Lines:
    split_id = line.split("'")
    id_db = split_id[1]
    split = line.split(",")
    check_id = split[9]
    project_id = split[10]
    sprint_id = split[11]
    kb_id = split[13]
    check_type = split[14]

    print("c = ChecklistResult('0','0',True)")
    print("c.checklist_id ="+check_id+"")
    print("c.project_id ="+project_id+"")
    print("c.sprint_id ="+sprint_id+"")
    print("c.kb_id ="+kb_id+"")
    print("c.checklist_type_id ="+check_type+"")
    print("db.session.add(c)")
    print("db.session.commit()")
    print("\n")