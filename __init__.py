# I am too lazy to add copyright. Just don't abuse any of this please.

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from globals import *                               # noqa: E402
from utils import EmbeddedBot                       # noqa: E402
from mycroft.skills.core import FallbackSkill       # noqa: E402
from mycroft.util.log import LOG                    # noqa: E402


__author__ = 'Fantailed'


class FallbackChatbot(FallbackSkill):
    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(FallbackChatbot, self).__init__(name="FallbackChatbot")
        self.aiml_bot = None
        self.client_context = None
        self.brain_loaded = False

    def initialize(self):
        # 0 is high priority, 100 is low
        self.register_fallback(self.handle_fallback, priority=90)

    def load_brain(self):
        LOG.info('Loading Brain')
        os.chdir(SKILL_PATH)
        # Initialize inner bot object
        self.aiml_bot = EmbeddedBot('config.yaml')
        self.client_context = self.aiml_bot.create_client_context("mycroft")
        os.chdir(MYCROFT_WORKING_DIR)

        self.brain_loaded = True

    def ask_brain(self, utterance):
        response = self.aiml_bot.process_question(self.client_context, utterance)
        return response

    def handle_fallback(self, message):
        if not self.settings.get("enabled") or self.settings.get("enabled") == 'true':
            if not self.settings.get("enabled"):
                print("Warning: Bot does not have a setting called 'enabled'!")
            if not self.brain_loaded:
                self.load_brain()
            utterance = message.data.get("utterance")
            answer = self.ask_brain(utterance)
            if answer != "":
                asked_question = False
                if answer.endswith("?"):
                    asked_question = True
                self.speak(answer, expect_response=asked_question)
                return True
        return False

    def shutdown(self):
        self.remove_fallback(self.handle_fallback)
        super(FallbackChatbot, self).shutdown()

    def stop(self):
        del self.aiml_bot
        return True


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return FallbackChatbot()
