from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('', views.ProductListAPIView.as_view()),
    path('test/', views.product_alt_view),
    path('<int:pk>/update/', views.ProductMixinView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view())
]
