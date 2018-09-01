import re
from skf.api.chatbot.scripts import entity_reco

vulndict=entity_reco.entity_data()
vulndict =  {k.lower(): v for k, v in vulndict.items()}
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def entity_recognizer(sentence):
    listofWords = re.findall(r"[\w']+|[.,!?;]", sentence)
    copyofWords=[]
    customentitiesDict = {}
    for l in listofWords:
        copyofWords.append(l)
    originalpos3 =[]
    #trigram
    i=-1
    j=-1
    while(i<len(listofWords)):
        i=i+1
        j=j+1
        originalpos3.append(i)
        if (i <len(listofWords)-2):
            s3 = listofWords[i]+' '+listofWords[i+1]+' '+listofWords[i+2]
            if (s3 in vulndict.keys()):
                originalpos3.pop()
                customentitiesDict[i,i+1,i+2] = s3
                copyofWords[j:j+3] = [vulndict[s3]]
                i=i+2
                originalpos3.append(i)
  
    #print(originalpos3)
    #print(copyofWords)
    #print(customentitiesDict)
    #bigram
    i=-1
    j=-1
    copyofWords2  =[]
    originalpos2 = []
    for w in copyofWords:
        copyofWords2.append(w)
    while(i<len(copyofWords)):
        i=i+1
        j=j+1
        originalpos2.append(originalpos3[i])
        if i<len(copyofWords)-1:
            s2 = copyofWords[i]+' '+copyofWords[i+1]
            if s2 in vulndict.keys():
                originalpos2.pop()
                customentitiesDict[originalpos3[i],originalpos3[i+1]] = s2
                copyofWords2[j:j+2] = [vulndict[s2]]
                i=i+1
                originalpos2.append(originalpos3[i])          
    #print(originalpos2)
    #print(copyofWords2)
    #print(customentitiesDict)
    i=0
    #unigram
        #if not copyofWords2:
        #   for l in listofWords:
        #      copyofWords2.apppend(l)
        # print ("yes")
    while (i<len(copyofWords2)): 
        if copyofWords2[i] in vulndict.keys():
            customentitiesDict[originalpos2[i]]= copyofWords2[i]
            copyofWords2[i] = vulndict[copyofWords2[i]]
        i=i+1
    #print(originalpos2)
    #print(copyofWords2)
    #print(customentitiesDict)
    for x in customentitiesDict:
        y=customentitiesDict[x]
        if y=="":
           return None
        else:
           return vulndict[y]
    #while()

#sent = input("enter text")
#print(entity_recognizer(sent.lower()))
