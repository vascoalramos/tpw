from django.urls import path

from hello_world import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("number/<int:num>/", views.number, name="number"),
    path("numbers/<int:num>/", views.number_2, name="numbers"),
]
