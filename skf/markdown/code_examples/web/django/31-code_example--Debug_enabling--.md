# Debug Enabling
-------

## Example:


    """
    Debug mode makes it a major security risk and therefore it must never be used on production machines. Django will display a detailed trace-back with more details about the application such 
    as Django settings
    """

    //The default settings.py file created by django-admin startproject sets DEBUG = True
    //It should be set to False in production 
    DEBUG = False