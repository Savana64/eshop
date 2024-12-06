from django.urls import path
from . import views

app_name = 'kdeco'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'), 
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    
    ]
