import logging
# https://www.geeksforgeeks.org/logging-in-python/#:~:text=Logging%20is%20a%20means%20of,the%20cause%20of%20the%20problem.

#5 logging levels
# Levels of Log Message
# There are five built-in levels of the log message.  

# Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info : These are used to confirm that things are working as expected
# Warning : These are used an indication that something unexpected happened, or is indicative of some problem in the near future
# Error : This tells that due to a more serious problem, the software has not been able to perform some function
# Critical : This tells serious error, indicating that the program itself may be unable to continue running

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#By default only messages with level above warning are printed 
# so warning, error and critical are printed

#we can change this by setting a basic configuration usually when importing

#It is good practice to create logger in your modules for easy debugging
logger = logging.getLogger(__name__) #this creates a logger with the name of the module (in this case its logging_m)
logger.info(f'This is from {__name__}')

#Look this up when writing software
#for now know that this exists

#look this section again later currently not needed
# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=8410s