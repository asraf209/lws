import logging

logname = '/var/log/lws/lws.log'
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


def log_error(error):
	logging.error(error)

def log_info(info):
	logging.info(info)

def log_debug(debug):
	logging.debug(debug)

def log_warning(warning):
	logging.warning(warning)
