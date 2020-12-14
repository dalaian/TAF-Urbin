import ConfigParser


class Config(object):

    config_path = "config/config.ini"

    def __init__(self):
        self.configParser = ConfigParser.RawConfigParser()
        self.configParser.read(self.config_path)

    def get_credentials(self, cred):
        """
        Gets an specific cred in under the section "USER"
        """
        return self.configParser.get('USER', cred)

    def get_user(self):
        """
        Gets the user
        """
        return self.get_credentials('u'), self.get_credentials('p')

    def get_base_url(self):
        """
        Gets the base url
        """
        return self.configParser.get("URLS", "base")

    def get_grid(self):
        """
        Gets the grid URL
        """
        return self.configParser.get("URLS", "seleniumAddress")
