"""djpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from djpro import views
from djpro import code


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage,name='home'),
    path("index.html", views.index,name='index'),
    path("aboutus.html", views.aboutus,name='about'),
    path("checkout.html", views.checkout,name='checkout'),
    path("shop.html", views.shop,name='shop'),
    path("contact.html", views.contact,name='contact'),
    path("login.html", views.login,name='login'),
    path("detail.html", views.detail,name='detail'),
    path("cart.html", views.cart,name='cart'),
    path("screen_time.html", code.screen_time),
    path("view_details.html",views.view_details),


]
