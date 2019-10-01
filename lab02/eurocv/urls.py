from django.conf.urls import url
from django.urls import path

from eurocv import views

urlpatterns = [
    url("person/(?P<name>.+)", views.render_cv, name="render_cv"),
]
