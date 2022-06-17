import subprocess, shutil, os, uuid, datetime

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def get_cheatsheets():
    git("clone", "https://github.com/OWASP/CheatSheetSeries.git")

    shutil.move("CheatSheetSeries/cheatsheets/", "../../Angular2/src/assets/training/owasp_cheatsheets/slides")
    shutil.move("CheatSheetSeries/assets/", "../../Angular2/src/assets/training/owasp_cheatsheets/assets")

get_cheatsheets()
