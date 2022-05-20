#CRITICAL 50
#ERROR 40
#WARNING 30
#INFO 20
#DEBUG 10
#NONSET 0

import logging


logging.basicConfig(
level=logging.DEBUG,
format= '{asctime} {levelname} {lineno} {message}',
style='{',
filename= '%slog' % __file__[:-2],
filemode= 'w'
)
loggy = logging.getLogger(__name__)



loggy.critical('This is a critical logging message')
loggy.error('This is an error logging message')
loggy.warning('This is an warning logging message')
loggy.debug('This is an debug logging message')
loggy.info('This is an info logging message')
