import configparser

config = configparser.ConfigParser()

config['default'] = {"API_ID": '25941753'}
with open('example.ini', 'w') as configfile:
    config.write(configfile)
