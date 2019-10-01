import os, nltk
from flask import Flask
from rake_nltk import Rake 

app = Flask(__name__)


def data():
    with open(os.path.join(app.root_path, "../datasets/entity_title.txt")) as title:
        title=title.readlines()
    return title


def phrase(ques):
    phrase1=[]
    new_list=[]
    r=Rake()
    question=ques
    r.extract_keywords_from_text(question)
    phrase1=r.get_ranked_phrases()
    for items in phrase1:
        new_list.extend(items.lower().split())
    return phrase1,new_list    


def lis(l):
    new_l=l
    ans=[]
    title=data()
    for i in new_l:
        i=i.lower().strip("\n")
        for t in title:
            t=t.lower()
            if i in t:
               ans.append(t.strip("\n"))
    ans=list(set(ans))
    return ans

   
def finalA(ques,ans):
    count=0
    for i in ans:
        i=i.strip("\n").lower()
        if i in ques.lower():
          if ques.lower() in i:
            count=count+1
            ent=i
            break
          else:
            count=count+1
            ent=i
            break
    if count==1:
        return ent
    else:
        if len(ans)==1:
           abc=ans[0]
           abc=abc.lower().strip("\n")
           return abc
        else:
           ansD={}
           #print("Select from these\n")
           for i in range(len(ans)):
               ansD[i+1]=ans[i]
           return ansD


def entity(ques):
    ph,list_p=phrase(ques)
    ans1=lis(ph)    
    ans=lis(list_p)
    y=finalA(ques,ans1)
    if len(ans1) == 0 and len(y) == 0:
       y=finalA(ques,ans)
       return y
    elif len(ans)==len(ans1):
       y=finalA(ques,ans)
       return y
    else:
       y=finalA(ques,ans1)
       return y

