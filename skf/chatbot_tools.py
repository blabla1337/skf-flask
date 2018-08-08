import os
from skf import settings
from flask import Flask


app = Flask(__name__)


def init_dataset():
    """Initializes the dataset needed for the chatbot."""
    try:
        print("do some magic for dataset generation")
        return True
    except:
        return False
