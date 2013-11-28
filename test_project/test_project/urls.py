from django.conf.urls import patterns, include, url
from django.views import generic

import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

try:
    from hvad_autocomplete import urls as hvad
except ImportError:
    # django 1.6 not support by hvad
    hvad = None

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^navigation/', include('navigation_autocomplete.urls')),
    url(r'^non_admin_add_another/',
        include('autocomplete_light.tests.apps.non_admin_add_another.urls')),
    (r'^$', generic.TemplateView.as_view(template_name='index.html'))
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
