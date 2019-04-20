"""
    FOR testing we are using sqlite memory which make its faster than actual database
"""
from project import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

#FAKE-KEY
SECRET_KEY = 'rtyutrew45676565qdfghy46543256764tewqqer4t54'


EMAIL_BACKEND = 'django.core.mail.bckends.locmem.EmailBackend'
