# Audit logs
-------

## Example:


    """
    Django uses Python’s builtin logging module to perform system logging. 

    Methods which should be logged : 
        - Data Addition
        - Data modification
        - Data deletion
        - Data Exports
        - Identifying security incidents
        - Perfomance monitoring etc

    Python logging configurations consists of four parts:

     - Loggers : is configured to have log level. Different log levels are DEBUG, INFO, 
                 WARNING, ERROR, CRITICAL. Each message that is written to the logger is a Log Record.
     - Handlers : It describes particular logging behaviour such as writing message on the screen, a file or to network socket.  
     - Filters : We can place an additional criteria for logging process.
     - Formatters : Formatters describe the exact format of that text.

    The logger module is inbuilt class in django for logging system information into files or sending logs through network.

    Different logging calls or mehtods : 
        - logger.debug()
        - logger.info()
        - logger.warning()
        - logger.error()
        - logger.critical()
        - logger.log()
        - logger.exception()
    """

    //Configuring loggers with app in SETTNGS.PY
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

    //Get Client IP

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    //Example for logging error
    import logging

    //Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, arg1, arg):
        ...
        if bad_mojo:
            //Log an error message
            logger.error('Something went wrong!' + get_client_ip(request)) 


    //Example for logging critical
    import logging

    //Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, arg1, arg):
        ...
        if security_violation:
            //Log an critical message
            logger.critical('Security violation!' + get_client_ip(request))