from django.urls import path
# from . import views
from .views import MachineListView, MachineDetailView, MachineCreateView, MachineUpdateView, MachineDeleteView, UserLogoutView


urlpatterns = [
    # Пример маршрутов для machines
    path('', MachineListView.as_view(), name='machine_list'),  # Список машин
    path('<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),  # Детали машины
    path('create/', MachineCreateView.as_view(), name='machine_create'),  # Создание машины
    path('<int:pk>/update/', MachineUpdateView.as_view(), name='machine_update'),  # Обновление машины
    path('<int:pk>/delete/', MachineDeleteView.as_view(), name='machine_delete'),  # Удаление машины
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Удаление машины
]
