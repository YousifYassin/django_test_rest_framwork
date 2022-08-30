from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='home'),
    path('vi/', views.vi, name='vi'),
    path('vi_ser/', views.vi_ser, name='vi_ser')
]
