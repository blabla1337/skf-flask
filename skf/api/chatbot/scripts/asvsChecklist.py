import json

def val(x):
    with open('datasets/asvslevel1.json') as json_file:  
            data = json.load(json_file)
            a=data['items']
    for i in range(0,len(a)):
            y=a[i]['checklist_items_checklistID'].split('.')
            if y[0]==x:
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

def val2(x):
    with open('datasets/asvslevel2.json') as json_file:  
            data = json.load(json_file)
            a=data['items']
    for i in range(0,len(a)):
            y=a[i]['checklist_items_checklistID'].split('.')
            if y[0]==x:
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])
def val3(x):
    with open('datasets/custom_git.json') as json_file:  
            data = json.load(json_file)
            a=data['items']
    for i in range(0,len(a)):
            y=a[i]['checklist_items_checklistID'].split('.')
            if y[0]==x:
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])


    
def checklist():
    print('Select the Checklist type:')
    print('1 ASVS LEVEL 1')
    print('2 ASVS LEVEL 2')
    print('3 Custom Git')
    user_option=int(input())
    if user_option==1:
        print("Do you want whole checklist? Y/N")
        user_ans=input()
        if user_ans=='y' or user_ans=='Y':
            with open('datasets/asvslevel1.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+"\n")
            print("Select your choice to see the description \n")


            user_optn=input()
            
            for i in range(0,len(a)):
                if str(user_optn).strip()==str(a[i]['checklist_items_checklistID']).strip():
                    return (a[i]['kb_items_content'])
                

        else:
            with open('datasets/asvslevel1.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                x=a[i]['checklist_items_checklistID'].split('.')
                if x[1]=='0':
                    print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+" y/n")
                    ui=input()
                    if ui=='y' or ui=='Y':
                        result=val(x[0])
                        return result
                        
                        
                    else:
                        pass
                     
    if user_option==2:
        print("Do you want whole checklist? Y/N")
        user_ans=input()
        if user_ans=='y' or user_ans=='Y':
            with open('datasets/asvslevel2.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

            print("Select your choice to see the description \n")


            user_optn=input()
            for i in range(0,len(a)):
                if str(user_optn).strip()==str(a[i]['checklist_items_checklistID']).strip():
                    return (a[i]['kb_items_content'])

                
        else:
            with open('datasets/asvslevel2.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                x=a[i]['checklist_items_checklistID'].split('.')
                if x[1]=='0':
                    print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+" y/n")
                    ui=input()
                    if ui=='y' or ui=='Y':
                        result=val2(x[0])
                        return result
                        
                    else:
                        pass
    if user_option==3:
        print("Do you want whole checklist? Y/N")
        user_ans=input()
        if user_ans=='y' or user_ans=='Y':
            with open('datasets/custom_git.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

            print("Select your choice to see the description \n")


            user_optn=input()
            for i in range(0,len(a)):
                if str(user_optn).strip()==str(a[i]['checklist_items_checklistID']).strip():
                    return (a[i]['kb_items_content'])

                
        else:
            with open('datasets/custom_git.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                x=a[i]['checklist_items_checklistID'].split('.')
                if x[1]=='0':
                    print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+" y/n")
                    ui=input()
                    if ui=='y' or ui=='Y':
                        result=val3(x[0])
                        return result
                        
                    else:
                        pass

                      
