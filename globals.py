import os
import sys

MYCROFT_WORKING_DIR = os.path.abspath(os.getcwd())
SKILL_PATH = os.path.dirname(os.path.abspath(__file__))
BOT_PATH = 'bots/BakaBot/'

sys.path.append(SKILL_PATH)
