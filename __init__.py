# I am too lazy to add copyright. Just don't abuse any of this please.

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from globals import *

from utils import EmbeddedBot
from mycroft.skills.core import FallbackSkill


__author__ = 'Fantailed'


class FallbackChatbot(FallbackSkill):
    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        os.chdir(SKILL_PATH)
        super(FallbackChatbot, self).__init__(name="FallbackChatbot")
        # Initialize inner bot object
        self.aiml_bot = None
        self.client_context = self.aiml_bot.create_client_context("mycroft")
        # os.chdir(MYCROFT_WORKING_DIR)

    def initialize(self):
        self.aiml_bot = EmbeddedBot('config.yaml')
        # 0 is high priority, 100 is low
        self.register_fallback(self.handle_fallback, priority=90)

    def ask_brain(self, utterance):
        response = self.aiml_bot.process_question(self.client_context, utterance)
        return response

    def handle_fallback(self, message):
        if not self.settings.get("enabled") or self.settings.get("enabled") == 'true':
            if not self.settings.get("enabled"):
                print("Warning: Bot does not have a setting called 'enabled'!")
            utterance = message.data.get("utterance")
            answer = self.ask_brain(utterance)
            if answer != "":
                asked_question = False
                if answer.endswith("?"):
                    asked_question = True
                self.speak(answer, expect_response=asked_question)
                return True
        return False

    # def shutdown(self):
    #     self.remove_fallback(self.handle_fallback)
    #     super(FallbackChatbot, self).shutdown()

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. Return True if it has been handled.
    def stop(self):
        del self.aiml_bot


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return FallbackChatbot()
