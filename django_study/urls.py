# django-debug-toolbar 사용하기 위한
# projects/urls.py 설정법

#1.

from django.conf import settings

#2.

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
     url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
