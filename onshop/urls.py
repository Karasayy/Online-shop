from django.urls import path
from .views import ProductList
from .views import ProductDetail
from .views import post_create
from .views import post_delete
from .views import post_update
from .views import Main
from .views import Contact
from .views import Shopping_cart
from .views import Checkout
from .views import SearchResultsView
from .views import rubric
from .views import home



urlpatterns = [
	path('rubric/<int:rubric_id>/', rubric, name='rubric'),
	path('main/', Main, name='main-page'),
	path('contact/', Contact, name='contact'),
	path('shopping_cart/', Shopping_cart, name='shopping-cart'),
	path('checkout/', Checkout, name='checkout'),
	path('products/', ProductList, name='product-list'),
	path('product/<int:pk>', ProductDetail.as_view(), name='product-detail'),
	path('product/create/', post_create, name='product-create'),
    path('product/<int:pk>/edit/', post_update, name='product-update'),
    path('product/<int:pk>/delete/', post_delete, name='product-delete'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('api/', home)
]
