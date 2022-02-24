from django.urls import path, include
from .views import wallet_view, authentication
from rest_framework.urlpatterns import format_suffix_patterns


url_patterns = [
    path(r'init', authentication.Authentication.as_view()),
    path(r'wallet', wallet_view.WalletBalanceApiView.as_view()),
    path(r'wallet/deposit', wallet_view.WalletDepositApiView.as_view()),
    path(r'wallet/withdrawal', wallet_view.WalletWithdrawalApiView.as_view()),
]
url_patterns = format_suffix_patterns(url_patterns)