from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('products/', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
