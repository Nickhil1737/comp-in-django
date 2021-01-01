from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import MyFormView
from .views import compxdet

urlpatterns = [
    path('',MyFormView.as_view(), name='compHome'),
    path('compxdet/<int:pk>',compxdet.as_view(), name='compxdet'),
]
