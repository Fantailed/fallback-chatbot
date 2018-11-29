import os
import sys
from programy.clients.events.console.client import ConsoleBotClient
from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.programy import ProgramyConfiguration
from programy.clients.args import CommandLineClientArguments


sys.path.append('venv/Lib/site-packages/programy')
sys.path.append('venv/Lib/site-packages/MetOffer-1.3.2.dist-info')


class EmbeddedBot(ConsoleBotClient):

    def __init__(self, config_filename):
        os.system('cls' if os.name == 'nt' else 'clear')
        os.chdir('bots/BakaBot/config/xnix')

        sys.argv = ['playground.py', '--config', 'config.yaml',
                    '--cformat', 'yaml', '--logging', 'logging.yaml']

        self._config_filename = config_filename
        ConsoleBotClient.__init__(self, "Console")

    def parse_arguments(self, argument_parser):
        client_args = CommandLineClientArguments(self, parser=None)
        return client_args

    def load_configuration(self, arguments):

        client_config = self.get_client_configuration()
        self._configuration = ProgramyConfiguration(client_config)

        yaml_file = YamlConfigurationFile()
        yaml_file.load_from_file(self._config_filename, client_config, ".")


if __name__ == '__main__':
    sys.argv = ['playground.py', '--config', 'config.yaml',
                '--cformat', 'yaml', '--logging', 'logging.yaml']
    bot = EmbeddedBot(sys.argv[2])

    client_context = bot.create_client_context("testUser")

    try:
        while True:
            question = input('>>>')
            response = bot.process_question(client_context, question)
            print(response)

    except KeyboardInterrupt:
        pass


