from django.urls import path
from . import views

urlpatterns = [
    # Пример маршрутов для maintenance
    path('', views.MaintenanceListView.as_view(), name='maintenance_list'),  # Список обслуживания
    path('<int:pk>/', views.MaintenanceDetailView.as_view(), name='maintenance_detail'),  # Детали обслуживания
    path('create/', views.MaintenanceCreateView.as_view(), name='maintenance_create'),  # Создание обслуживания
    path('<int:pk>/update/', views.MaintenanceUpdateView.as_view(), name='maintenance_update'),  # Обновление обслуживания
    path('<int:pk>/delete/', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),  # Удаление обслуживания
]
