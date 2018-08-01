import json, nltk, os
from flask import Flask, jsonify, request
from nltk.stem.lancaster import LancasterStemmer
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from skf.api.chatbot.scripts import intent_classifier
from skf.api.chatbot.scripts import entity_classifier1
from skf.api.chatbot.scripts import entity_classifier2
from skf.api.chatbot.scripts import code_classify
from skf.database import db
from skf.database.chatbot_logs import chatbot_post

app = Flask(__name__)

def des_sol(question,intent):
        entity=entity_classifier1.entity_recognizer(question.lower())
        if entity is None:
           entity=entity_classifier2.entity(question)
        intent=intent
        read_file = open(os.path.join(app.root_path, "datasets/desc_sol.json"), 'r')
        data = json.load(read_file)
        ite=data['items']
        if type(entity)==str:
            for d in ite:
                 if entity.lower()==d['title'].lower():
                      if intent=="Description":
                          desc="Description for "+d['title']+" is : "+ d[intent]
                          intent="NULL"
                          return desc
                          break
                      else:
                          sol="Solution for "+d['title']+" is : "+ d[intent]
                          intent="NULL"
                          return sol
                          break
        else:
             if len(entity)>0:
                for i in entity:
                    entity[i]=intent+" "+entity[i]
                return entity
             else:
                log=open(os.path.join(app.root_path,"logs.txt"),"a") 
                msg="Please be more specific"
                log.write(question+"\n")
                log.close()
                return msg

def code(question,intent,language):
        code_entity=code_classify.entity(question)
        read_file = open(os.path.join(app.root_path, "datasets/code_data.json"), 'r')
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
                       code_a="Code for "+ d['content']+"\n Code language is " + d['code_lang']
                       count=count+1
                       return code_a
            if count==0:
                    ent={}
                    for i in range(len(code_languages)):
                        entity=intent+" "+str(code_entity[0].strip("\n").lower())+" in "+code_languages[i]
                        print(entity)
                        ent[i]=entity
                    return ent
                    for d in code_ite:
                        if entity==d['title'].lower() and lang in code_languages:
                              if lang==d['code_lang'].lower():
                                 return d['content']
                                 count=count+1
        else:
             if language is None:
               language=str(code_entity[-1].strip("\n").lower())
             elif language:
               language=language
             else:
                #db.execute("INSERT INTO chatbot_logs (question)VALUES ('question')");
                log=open(os.path.join(app.root_path,"logs.txt"),"a") 
                msg="Please be more specific"
                result = chatbot_post(question)
                db.session.add(result)
                db.session.commit()
                log.write(question+"\n")
                log.close()
                return msg
             code_list={}
             for i in code_entity[0]:
                 code_list[i]=intent+" "+code_entity[0][i]
             return code_list
