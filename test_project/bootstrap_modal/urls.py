from django.urls import re_path
from django.views.generic.base import TemplateView
from autocomplete_light.compat import urls, url

urlpatterns = urls([
    re_path(r'^$', TemplateView.as_view(template_name="bootstrap_modal/modal.html"), name="bootstrap_modal"),
])
