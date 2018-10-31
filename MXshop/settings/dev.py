from MXshop.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root1234',
        'NAME': 'mxshop_local',
        'OPTIONS': {'charset': 'utf8',
                    "init_command": "SET default_storage_engine=INNODB;"},
    },
}
