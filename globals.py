"""
This file holds all the values that are shared between the Mycroft skill interface and the Program-Y bot content.
"""

import os

MYCROFT_WORKING_DIR = os.path.abspath(os.getcwd())
SKILL_PATH = os.path.dirname(os.path.abspath(__file__))
BOT_PATH = 'bots/BakaBot/'
