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
from Bank_database.views.main import main
from Bank_database.views.add_currency_to_account import add_currency_to_account
from Bank_database.views.error_404 import error_404
from Bank_database.views.invest_money import invest_money
from Bank_database.views.lend_money import lend_money
from Bank_database.views.list_lendings import list_lendings
from Bank_database.views.list_your_taken_money import list_your_taken_money
from Bank_database.views.logged import logged
from Bank_database.views.my_investments import my_investments
from Bank_database.views.register import register
from Bank_database.views.transaction_list_for_user import transaction_list_for_user
from Bank_database.views.withdraw_currency_from_account import withdraw_currency_from_account

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
    path('my-investments/',my_investments, name='my_investments'),
    path('invest_money/<int:id>/',invest_money,name='invest_money'),
    path('widthdrawn/', withdraw_currency_from_account, name="widthdrawn"),
    path('transaction_list/',transaction_list_for_user, name="transaction_list")
]
#Error Handling with 404
handler404 = "Bank_database.views.error_404.error_404"