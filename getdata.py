import codecs
import configparser

config = configparser.ConfigParser()


# Get receivers e-mail addresses
def get_receivers(path):
    with open(path, 'r') as receivers:
        recs = receivers.readline()
        recs = recs.splitlines()
        return recs


# Read email subject and content from file
def get_email(path):
    with codecs.open(path, encoding='utf-8') as email:
        subject = email.readline()
        content = email.read()
        return subject, content


# Get metadata for server connection
def get_metadata():
    config.read('properties.ini')
    server = config['PROPERTIES']['SERVER']
    port = int(config['PROPERTIES']['PORT'])
    sender = config['PROPERTIES']['SENDER_ADDR']
    password = config['PROPERTIES']['PASSWORD']
    return server, port, sender, password


# Get the file to read email form
def get_mailpath():
    config.read('properties.ini')
    return config['PROPERTIES']['MAIL_PATH']


# Insert initial data to properties.ini, optional
def insert_data():
    config['PROPERTIES'] = {
        'SERVER': 'add value',
        'PORT': 'add value',
        'SENDER_ADDR': 'add value',
        'PASSWORD': 'add value',
        'MAIL_PATH': 'email.txt',
        'RECEIVER_PATH': 'receivers.txt',
    }
    with open('properties.ini', 'w') as configfile:
        config.write(configfile)


def get_recpath():
    config.read('properties.ini')
    return config['PROPERTIES']['RECEIVER_PATH']
