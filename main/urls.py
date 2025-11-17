from django.contrib import admin
from django.urls import path

from testapp import views as testapp_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", testapp_views.home, name="home"),
]
