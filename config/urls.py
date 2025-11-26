from django.contrib import admin
from django.urls import path, include

from study import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("study.urls")),
]
