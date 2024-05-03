"""
URL configuration for testproject project.

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
from TestApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home),
                  path('view/<int:id>', views.views, name='view'),
                  path('login', views.login, name='login_page'),
                  path("add", views.cart, name='cart'),
                  path("cart", views.add_to_cart, name='addcart'),
                  path('shop', views.shopping, name='buy'),
                  path('review', views.add_review, name='review_add'),
                  path('addbook/', views.addbook, name='add_book'),
                  path('user_profile/', views.profile, name='view_profile'),
                  path('user_profile/delete/<int:id>', views.delete_book),
                  path('user_profile/edit/<int:id>', views.edit_book)

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
