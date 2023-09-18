# django-debug-toolbar 사용하기 위한
# Projects/settings.py 필수 설정법

#1.
DEBUG = True

#2.

INSTALLED_APPS = [
     'debug_toolbar',

]

#3.

MIDDLEWARE =[

  'debug_toolbar.middleware.DebugToolbarMiddleware',
]

#4.

TEMPLATES=[

  'APP_DIRS': True, #True로 설정
]

#5.

STATIC_URL = '/static/' 

