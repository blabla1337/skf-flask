# Audit logs
-------

## Example:


    """
    Django uses Python’s builtin logging module to perform system logging. 

    Python logging configurations consists of four parts:

     - Loggers : is configured to have log level. Different log levels are DEBUG, INFO, 
                 WARNING, ERROR, CRITICAL. Each message that is written to the logger is a Log Record.
     - Handlers : It describes particular logging behaviour such as writing message on the screen, a file or to network socket.  
     - Filters : We can place an additional criteria for logging process.
     - Formatters : Formatters describe the exact format of that text.
    """

    # Using Logging
    # import the logging library
    
    import logging

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, arg1, arg):
        ...
        if bad_mojo:
            # Log an error message
            logger.error('Something went wrong!') 

    """
    Different logging calls : 
        - logger.debug()
        - logger.info()
        - logger.warning()
        - logger.error()
        - logger.critical()
        - logger.log()
        - logger.exception()
    """


    # Configuring loggers with app in SETTNGS.PY
    """
    This creates polls app log file polls.log
    """
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
            },
            'applogfile': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(DJANGO_ROOT, 'polls.log'),
                'maxBytes': 1024*1024*15, # 15MB
                'backupCount': 10,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'polls': {
                'handlers': ['applogfile',],
                'level': 'DEBUG',
            },
        },
    }