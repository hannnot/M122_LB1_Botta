import configparser
from configparser import ConfigParser
from methods import openEmail, sendEmail, createOutput

config = configparser.ConfigParser()
config.read('config.ini')

sendEmail(config, openEmail(config))
createOutput(config, openEmail(config))