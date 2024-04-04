from django.urls import re_path

from autocomplete_light.compat import url, urls
from .views import navigation_autocomplete

urlpatterns = urls([
    re_path(r'^$', navigation_autocomplete, name='navigation_autocomplete'),
])
