from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileUpdateView, UserPasswordChangeView


urlpatterns = [
    # Пример маршрутов для управления учетными записями
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'), 
]

# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# # from .views import BaseRegisterView
# # from .views import upgrade_me

# urlpatterns = [
#     path('login/',
#          LoginView.as_view(template_name = 'sign/login.html'),
#          name='login'), #http://127.0.0.1:8000/sign/login/
#     path('logout/',
#          LogoutView.as_view(template_name = 'sign/logout.html'),
#          name='logout'), #http://127.0.0.1:8000/sign/logout/
#     # path('signup/',
#     #      BaseRegisterView.as_view(template_name='sign/signup.html'),
#     #      name='signup'),  #http://127.0.0.1:8000/sign/signup/
#     # path('upgrade/', upgrade_me, name = 'upgrade')
# ]