import json, nltk, os

from flask import Flask, jsonify, request
from nltk.stem.lancaster import LancasterStemmer
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from skf.api.chatbot.scripts import intent_classifier
from skf.api.chatbot.scripts import entity_classifier1
from skf.api.chatbot.scripts import entity_classifier2
from skf.api.chatbot.scripts import code_classify

app = Flask(__name__)

def answer(question):
        intent=intent_classifier.predict(question)
        if intent=="Description" or intent=="Solution":
                   y=des_sol(question,intent)
                   return y
        else:
                   lang=None
                   code(question,intent,lang)


def des_sol(question,intent):
        entity=entity_classifier1.entity_recognizer(question.lower())
        if entity is None:
           entity=entity_classifier2.entity(question)
      
        read_file = open(os.path.join(app.root_path, "datasets/desc_sol.json"), 'r')
        data = json.load(read_file)
        ite=data['items']
        if type(entity)==str:
            for d in ite:
                 if entity.lower()==d['title'].lower():
                      if intent=="Description":
                          desc="Description for "+d['title']+" is : "+ d[intent]
                          intent="NULL"
                          print(desc)
                          return desc
                          break
                      else:
                          sol="Solution for "+d['title']+" is : "+ d[intent]
                          intent="NULL"
                          return sol
                          break
        else:
             if len(entity)>0:
                print("Please select from these options ")
                for i in entity:
                    print(str(i)+":"+entity[i])
                #TO_BE_CHANGEDn=int(input("enter your choice "))
                #n=int(n)
                question=entity[n]
                des_sol(question,intent)
             else:
                print("Please be more specific ")
                question=input("enter your question again ")
                answer(question)


def code(question,intent,language):
        code_entity=code_classify.entity(question)
        read_file = open(os.path.join(app.root_path, "api/chatbot/datasets/code_data.json"), 'r') 
        code_data = json.load(read_file)
        code_ite=code_data['items']
        code_languages=[]
        count=0
        if len(code_entity)==2 and type(code_entity[0])==str:
            entity=str(code_entity[0].strip("\n").lower())
            if language is None:
               language=str(code_entity[-1].strip("\n").lower())
            else:
               language=language
            for d in code_ite:
                 if entity==d['title'].lower():
                    code_languages.append(d['code_lang'])
            for d in code_ite:
                 if entity==d['title'].lower() and language in code_languages:
                    if language==d['code_lang'].lower():
                       print("Code for "+ d['content'])
                       print("\n Code language is " + d['code_lang'])
                       count=count+1
            if count==0:
                    code_l={}
                    entity=str(code_entity[0].strip("\n").lower())
                    for i in range(len(code_languages)):
                        code_l[i+1]=code_languages[i]      
                    print("The language you typed is not availabe. Select from the following:")
                    for i in code_l:
                        print(str(i)+":"+code_l[i])
                    #TO_BE_CHANGEDn=int(input("Enter your choice: "))
                    lang=code_l[n]
                    for d in code_ite:
                        if entity==d['title'].lower() and lang in code_languages:
                              if lang==d['code_lang'].lower():
                                 print("Code for "+ d['content'])
                                 print("\n Code language is " + d['code_lang'])
                                 count=count+1
            #TO_BE_CHANGEDques=input("\n Do you have more Questions Y/N ")
            if(ques=="y" or ques=="Y"):
                   #TO_BE_CHANGEDquestion=input("Enter new question ")
                   answer(question)
            else:
                   print("Thanks for using")
        else:
             if language is None:
               language=str(code_entity[-1].strip("\n").lower())
             else:
               language=language
             print("Please select from these options ")
             for i in code_entity[0]:
                 print(str(i)+":"+code_entity[0][i])
             #TO_BE_CHANGEDn=int(input("enter your choice "))
             question=code_entity[0][n]
             code(question,"Code",language)
#TO_BE_CHANGEDquestion=input("Enter Question ")
#TO_BE_CHANGED
#question=request.form.get('question')
#answer(question)

