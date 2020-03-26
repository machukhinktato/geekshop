from adminapp.views import (
    user_delete, user_update, product_update, user_create,
    product_create, products, categories, product_delete
)
from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'


urlpatterns = [
    path('users/create/', user_create, name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(),
         name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]