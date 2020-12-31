from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import MyFormView

urlpatterns = [
    path('',MyFormView.as_view(), name='compHome'),
    path('compxdet/', views.compxdet, name='compxdet'),
]
