#CRITICAL 50
#ERROR 40
#WARNING 30
#INFO 20
#DEBUG 10
#NONSET 0

import logging

logging.basicConfig(
level=logging.DEBUG,
format= '{asctime} {levelname} {message}',
style='{'
)

logging.critical('This is a critical logging message')
logging.error('This is an error logging message')
logging.warning('This is an warning logging message')
logging.debug('This is an debug logging message')
logging.info('This is an info logging message')
