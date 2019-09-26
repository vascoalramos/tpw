from django.urls import path
from django.conf.urls import url

from eurocv import views

urlpatterns = [
    url("eurocv/(?P<name>.+)", views.render_cv, name="render_cv"),
]