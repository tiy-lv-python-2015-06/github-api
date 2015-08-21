from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>[0-9a-zA-Z]+)/', 'gitpage.views.get_profile')
]
