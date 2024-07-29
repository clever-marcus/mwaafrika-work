from django.urls import path
from user.views import loginView, registerView, CookieTokenRefreshView, logoutView, user, index, wallet_balance

app_name = "user"

urlpatterns = [
    path('', index, name='index'), # added path for index.html file in build file
    path('login', loginView, name='login'),
    path('register', registerView, name='register'),
    path('refresh-token', CookieTokenRefreshView.as_view(), name='refresh_token'),
    path('logout', logoutView, name='logout'),
    path('user', user, name='user'),
    path('wallet_balance', wallet_balance, name='wallet_balance'),
]
