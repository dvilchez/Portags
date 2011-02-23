from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^portags/', include('portags.urls')),
    (r'^admin/', include(admin.site.urls)),
)