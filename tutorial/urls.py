import os

from django.conf.urls import include, url

base_urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# Adjust URLs for base_url
FUNCTIONS_MOUNT_POINT = os.getenv('FUNCTIONS_MOUNT_POINT')
urlpatterns = [
    url(FUNCTIONS_MOUNT_POINT + '/', include(base_urlpatterns)),
]
