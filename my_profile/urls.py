from . import views
from django.urls import path

app_name = "profile"

urlpatterns = [
    path('', views.about, name='about'),
]
