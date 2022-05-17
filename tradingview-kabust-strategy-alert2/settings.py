import configparser

# from utils.utils import bool_from_str


conf = configparser.ConfigParser()
conf.read('settings.ini')

apiKey = conf['kabustation']['apiKey']
password = conf['kabustation']['password']