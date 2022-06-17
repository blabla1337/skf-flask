import subprocess, shutil, os, uuid, datetime

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def get_pro_active():
    git("clone", "https://github.com/OWASP/www-project-proactive-controls.git")

    shutil.move("www-project-proactive-controls/v3/en/", "../../Angular2/src/assets/training/owasp_pro_active/slides")

get_pro_active()
