from django.urls import path
from . import views


urlpatterns = [
      path('novo/', views.novo, name='novo'),
      path('', views.home, name='home')
] 