"""
URL configuration for campus_eats project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from campus_eats import views
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page,name='login'),
    path('home/',views.home_page,name='home'),
    path('about/',views.about),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.cart_page),
    path('generate-upi-link/',views.generate_upi_link),
    path('payment-success/', views.payment_success),
    path('items/<str:type>/',views.items_display),
    path('logout/',views.logout_user),
    path('update_profile/',views.update),
    path('cart_add/',views.add_to_cart),
    path('remove_item/',views.remove),
    path('update_quantity/',views.update_quantity),
    path('contact/',views.contact_page),
    path('submit_query/',views.submit)
]

if settings.DEBUG == True:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


