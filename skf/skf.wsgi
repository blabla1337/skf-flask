import sys, os
path = os.path.abspath(os.path.dirname(__file__))
if path not in sys.path:
    print "Inserting path " + path
    sys.path.insert(0, path)
os.chdir(path)
from skf import app as application

