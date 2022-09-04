from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home, name='home'),
    path('vi/', views.vi, name='vi'),
    path('vi_ser/', views.vi_ser, name='vi_ser')
]
