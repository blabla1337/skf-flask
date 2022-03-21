import subprocess, shutil, os, uuid, datetime

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def get_wstg():
    #shutil.rmtree("wstg")
    git("clone", "https://github.com/OWASP/wstg.git")

    shutil.move("wstg/document/2-Introduction", "../../Angular2/src/assets/training/security_testing/slides")
    shutil.move("wstg/document/3-The_OWASP_Testing_Framework", "../../Angular2/src/assets/training/security_testing/slides")
    shutil.move("wstg/document/4-Web_Application_Security_Testing", "../../Angular2/src/assets/training/security_testing/slides")
    shutil.move("wstg/document/5-Reporting", "../../Angular2/src/assets/training/security_testing/slides")


#get_wstg()

def print_head():
    x = datetime.date.today()
    head = """
    id: """+str(uuid.uuid4())+"""
    version: 2.1
    date: """+x.strftime("%d/%m/%Y")+"""
    name: Web/API Security testing
    languages:
    - python
    content:
    - slide: Angular2/src/assets/training/security_testing/slides/1-Landing/Landing.md
    topics:
    """
    print(head)

def create_topic_intro():
    content = """  - id: """+str(uuid.uuid4())+"""
    name: Introduction WSTG
    content:
      - video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    categories:
    """
    content += """      - id: """+str(uuid.uuid4())+"""
    name: The OWASP Testing Project
    content:
        - slide: Angular2/src/assets/training/security_testing/slides/2-Introduction/README.md
        - questionnaire: Angular2/src/assets/training/security_testing/questionnaire/2.md
        """
    
    content += """  - id: """+str(uuid.uuid4())+"""
    name: Penetation testing
    content:
      - video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    categories:
    """
    content += """      - id: """+str(uuid.uuid4())+"""
    name: The Web Security Testing Framework
    content:
        - slide: Angular2/src/assets/training/security_testing/slides/3-The_OWASP_Testing_Framework/0-The_Web_Security_Testing_Framework.md
        - questionnaire: Angular2/src/assets/training/security_testing/questionnaire/2.md"""
    content += """      - id: """+str(uuid.uuid4())+"""
    name: Penetration Testing Methodologies
    content:
        - slide: Angular2/src/assets/training/security_testing/slides/3-The_OWASP_Testing_Framework/1-Penetration_Testing_Methodologies.md
        - questionnaire: Angular2/src/assets/training/security_testing/questionnaire/2.md
        """
    
    content += """  - id: """+str(uuid.uuid4())+"""
    name: Penetration testing reporting
    content:
      - video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    categories:
    """
    content += """      - id: """+str(uuid.uuid4())+"""
    name: The report approach
    content:
        - slide: Angular2/src/assets/training/security_testing/slides/5-Reporting/README.md
        - questionnaire: Angular2/src/assets/training/security_testing/questionnaire/1.md
        """
    print(content)

def create_checklist(path):
    x = path.split("/")
    file_edit = x[9][3:]
    name = file_edit.replace("_", " ")
    content = """
      - id: """+str(uuid.uuid4())+"""
    name: """+name+"""
    content:
        - video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    categories:
    """
    folder = os.listdir(path)
    file_md = path[6:]
    for filename in folder:
        file_edit = filename[3:]
        name = file_edit.replace("_", " ")
        content += """
              - id: """+str(uuid.uuid4())+"""
        name: """+name+"""
        content:
        - slide: """+file_md+"/"+filename+"""
        - questionnaire: Angular2/src/assets/training/security_testing/questionnaire/1.md
        - lab:
            hint: ZZZZZZZ
            writeup: XXXXXXX
            images:
                - python: blabla1337/owasp-skf-lab-py"""
        print(content)



get_wstg()