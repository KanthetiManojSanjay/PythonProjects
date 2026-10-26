import logging

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
logging.critical("Critical") #Highest
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug") #Lowest
