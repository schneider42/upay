import ConfigParser
import sys
import logging

import nupay
logging.basicConfig(level=logging.DEBUG)
config = ConfigParser.RawConfigParser()
config_file = sys.argv[1]
config.read(config_file)


nupay.SessionManager(config).bootstrap_db()
 
