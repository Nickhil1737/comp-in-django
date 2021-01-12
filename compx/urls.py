from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import MyFormView
from .views import MyFormView2
from .views import compxdet
from .views import homepage
from .views import compxcompare
from .views import exceptionview

urlpatterns = [
    path('',homepage.as_view(), name='index'),
    path('compform',MyFormView.as_view(), name='compHome'),
    path('compexp',exceptionview.as_view(), name='compexp'),
    path('compformt',MyFormView2.as_view(), name='compHomet'),
    path('compxdet/<int:pk>',compxdet.as_view(), name='compxdet'),
    path('compxcompare/<int:pk>/<int:pkk>',compxcompare.as_view()),
]
