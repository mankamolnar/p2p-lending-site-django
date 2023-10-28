"""Bank URL Configuration

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
from django.urls import path, include
from Bank_database.views import register, main , add_currency_to_account , logged, list_lendings,lend_money


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('user_example.urls')) saját url-ek
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', register, name='registration'),
    #Custom login:
    path('login/',logged, name="custom_login"),
    path('', main, name="main_page"),
    path('addtobalance/',add_currency_to_account,name='add_currency'),
    path('list-lendings/',list_lendings,name='list_lendings'),
    path('lend_money/',lend_money,name='lend_money'),
]
#Error Handling with 404
handler404 = "Bank_database.views.error_404"