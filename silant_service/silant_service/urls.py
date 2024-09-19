# silant_service/urls.py - корневой маршрут
from django.contrib import admin
from django.urls import path, include
from machines.views import HomePageView, UserLogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для административной панели Django
    path('api/machines/', include('machines.urls')),  # Маршрут для API machines
    path('api/maintenance/', include('maintenance.urls')),  # Маршрут для API maintenance
    path('api/complaints/', include('complaints.urls')),  # Маршрут для API complaints
    path('accounts/', include('accounts.urls')),  # Маршрут для API accounts (регистрация, вход и т.д.)
    path('', login_required(HomePageView.as_view()), name='home'),
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Удаление машины
]

