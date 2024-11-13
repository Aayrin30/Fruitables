"""
URL configuration for my_main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('rating', views.rating, name='rating'),

    path('shop_detail1/<int:id>', views.shop_detail1, name='shop_detail1'),
    path('shop_detail', views.shop_detail, name='shop_detail'),

    path('testimonial', views.testimonial, name='testimonial'),
    path('contact', views.contact, name='contact'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('orders', views.orders, name='orders'),
    path('orderhandle/<int:id>', views.orderhandle, name='orderhandle'),

    path('emptycart', views.emptycart, name='emptycart'),
    path('search', views.search, name='search'),

    path('cart', views.cart, name='cart'),

    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('increment/<int:id>', views.increment, name='increment'),
    path('decrement/<int:id>', views.decrement, name='decrement'),
    path('handle/<int:id>', views.handle, name='handle'),

    path('error', views.error, name='error'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forget', views.forget, name='forget'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    path('price_filter', views.price_filter, name='price_filter'),
    path('wishlist/<int:id>', views.wishlist, name='wishlist'),
    path('show_wishlist', views.show_wishlist, name='show_wishlist'),
    path('wishlist_handle/<int:id>', views.wishlist_handle, name='wishlist_handle'),

    path('profile', views.profile, name='profile'),
    path('password', views.password, name='password'),

    # path('profile1/<int:id>', views.profile1, name='profile1'),







]
