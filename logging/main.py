import logging

#? logging docs
#? https://docs.python.org/3/library/logging.html#logrecord-attributes

# order of importance
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning') #by def level in consol
# logging.error('error')
# logging.critical('critical')


# configure logging
# only do one time at the start
logging.basicConfig(level=logging.DEBUG, filemode='w', filename='logging/log.log', #logging everithing from this level and above
                    format="%(asctime)s - %(levelname)s - %(message)s") 


logging.debug('debug')
logging.info('info')
logging.warning('warning') #by def level in consol
logging.error('error')
logging.critical('critical')


try:
    1/ 0
except ZeroDivisionError as e:
    logging.error("Error: %s", e, exc_info=True)