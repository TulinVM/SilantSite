from django.urls import path
from .import views

urlpatterns = [
    # Пример маршрутов для complaints
    path('', views.ComplaintListView.as_view(), name='complaint_list'),  # Список жалоб
    path('<int:pk>/', views.ComplaintDetailView.as_view(), name='complaint_detail'),  # Детали жалобы
    path('create/', views.ComplaintCreateView.as_view(), name='complaint_create'),  # Создание жалобы
    path('<int:pk>/update/', views.ComplaintUpdateView.as_view(), name='complaint_update'),  # Обновление жалобы
    path('<int:pk>/delete/', views.ComplaintDeleteView.as_view(), name='complaint_delete'),  # Удаление жалобы
]
