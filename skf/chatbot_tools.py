import os
from skf import settings
from flask import Flask
from api.chatbot.dataset_prepare import data

app = Flask(__name__)


def init_dataset():
    """Initializes the dataset needed for the chatbot."""
    try:
        data.extract_from_api()
        data.desc_sol_data()
        data.entity_data()
        data.intent_data()
        data.code_entity()
        return True
    except:
        return False
