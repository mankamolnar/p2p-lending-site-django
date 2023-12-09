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
import Bank_database.views as viewer

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('user_example.urls')) saját url-ek
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', viewer.register, name='registration'),
    #Custom login:
    path('login/',viewer.logged, name="custom_login"),
    path('', viewer.main, name="main_page"),
    path('addtobalance/',viewer.add_currency_to_account,name='add_currency'),
    path('list-lendings/',viewer.list_lendings,name='list_lendings'),
    path('lend_money/',viewer.lend_money,name='lend_money'),
    path('my-investments/', viewer.my_investments, name='my_investments'),
    path('invest_money/<int:id>/',viewer.invest_money,name='invest_money'),
    path('widthdrawn/', viewer.withdraw_currency_from_account, name="widthdrawn"),
    path('transaction_list/',viewer.transaction_list_for_user, name="transaction_list")
]
#Error Handling with 404
handler404 = "Bank_database.views.error_404"