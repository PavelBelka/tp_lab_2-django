from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet, basename='api-product')

urlpatterns = [
    path('', views.index, name =  'index'),
    path('register/', views.register, name = 'register'),
    path('mypurchase/', views.my_purchase, name = 'mypurchase'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    *router.urls
]