import subprocess, shutil, os, uuid, datetime

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def get_top10():
    git("clone", "https://github.com/OWASP/Top10.git")

    shutil.move("Top10/2021/docs/assets", "../../Angular2/src/assets/training/owasp_top10/slides")

get_top10()

