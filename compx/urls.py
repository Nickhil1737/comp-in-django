from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.compHome, name='compHome'),
    path('compxdet/', views.compxdet, name='compxdet'),
]
