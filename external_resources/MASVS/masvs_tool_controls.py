import json
import re    
        
with open('masvs.json') as json_file:
    data = json.load(json_file)
    print("        '''")
    print("        Checklist Categories for MASVS")
    print("        '''")
    print("\r\n")
    for p in data:
        for r in p['requirements']:
            id = r['id']
            links = ""
            try:
                links_raw = r['links']
                for l in links_raw:
                    links += l+"," 
            except KeyError:
                links = ""
            links = links[:-1]
            text = r['text'].replace("'", "\\'")
            checklist_type_raw = r['id'].split(".")
            #add 14 as MASVS start at checklist_type 15 in SKF DB
            checklist_type = int(checklist_type_raw[0]) + 14
            if r['L2'] == True:
                maturity = '2'            
            if r['L1'] == True:
                maturity = '1'
            if r['R'] == True:
                maturity = '3'
            maturity
            print("        c = ChecklistKB('"+id+"', '"+text+"', "+str(checklist_type)+", False, '"+links+"', "+maturity+")")
            print("        c.kb_id = 2000")
            print("        db.session.add(c)")
            print("        db.session.commit()")
            print("\r\n")
        
        
        
