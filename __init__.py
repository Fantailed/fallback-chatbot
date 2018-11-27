# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from mycroft.skills.core import FallbackSkill
from utils import EmbeddedBot


# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class FallbackChatbot(FallbackSkill):
    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(FallbackChatbot, self).__init__(name="FallbackChatbot")
        # Initialize inner bot object
        self.aiml_bot = EmbeddedBot('bot/BakaBot/config/windows/config.yaml')
        self.client_context = self.aiml_bot.create_client_context("mycroft")

    def initialize(self):
        # 0 is high priority, 100 is low
        self.register_fallback(self.handle_fallback, priority=90)

    def ask_brain(self, utterance):
        response = self.aiml_bot.process_question(self.client_context, utterance)
        # TODO: backup copy blabla
        return response

    def handle_fallback(self, message):
        if self.settings.get("enabled") == 'true':
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

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. Return True if it has been handled.
    def stop(self):
        pass


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return FallbackChatbot()
