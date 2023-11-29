from . import views
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static

app_name = "produtos"

urlpatterns = [
    path("home/", views.index, name='Home')
]