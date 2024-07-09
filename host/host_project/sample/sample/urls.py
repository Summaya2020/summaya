"""
URL configuration for sample project.

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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    #url data  passing
    # path('urlpass/<d>',views.urlpass),
    path('urlpass/<int:d>',views.urlpass),
    path('home',views.home),
    path('ind',views.ind),
    path('',views.index),
    path('reg',views.reg),
    path('login',views.login),
    path('userhome',views.userhome),
    path('adminhome',views.adminhome),
    path('viewuser',views.view_user),
    path('add_product',views.add_product),
    path('manage_product',views.manage_product),
    path('update_product/<int:d>',views.update_product),
    path('logout',views.logout),
    path('add_cart/<int:d>',views.add_cart),
    path('display_cart',views.display_cart),
    path('remove_cart/<int:d>',views.remove_cart),
    path('add_wishlist/<int:d>',views.add_wishlist),
    path('display_wishlist',views.display_wishlist),
    path('remove_wishlist/<int:d>',views.remove_wishlist),
    path('increment/<int:d>',views.increment),
    path('decrement/<int:d>',views.decrement),
    path('payment/<int:d>',views.payment),
    path('success',views.success),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)