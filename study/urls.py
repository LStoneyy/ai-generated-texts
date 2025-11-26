from django.urls import path
from . import views

app_name = "study"

urlpatterns = [
    path("", views.start, name="start"),
    path("task/<int:index>/", views.classify, name="classify"),
    path("finish/", views.finish, name="finish"),
    path("impressum/", views.impressum, name="impressum"),
    path("datenschutz/", views.datenschutz, name="datenschutz"),
]
