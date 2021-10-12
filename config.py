import configparser


class Config:
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding='utf-8')

    def get(self, section, name):
        return self.config.get(section, name)


config = Config()
