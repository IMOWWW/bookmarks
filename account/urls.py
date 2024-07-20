from django.urls import path
from .views import user_login, dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
]


