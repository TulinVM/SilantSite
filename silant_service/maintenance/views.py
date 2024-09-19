from django.shortcuts import render

# Create your views here.
# Представления для модели Maintenance (ТО)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Maintenance
from machines.models import Machine  # Импорт модели Machine


class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'silant_service/maintenance_list.html'
    context_object_name = 'maintenance_list'  # Имя переменной в шаблоне

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.all()  # Получение всех объектов Machine и добавление их в контекст
        return context

class MaintenanceDetailView(DetailView):
    model = Maintenance
    template_name = 'silant_service/maintenance_detail.html'

class MaintenanceCreateView(CreateView):
    model = Maintenance
    fields = '__all__'
    template_name = 'silant_service/maintenance_form.html'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    fields = '__all__'
    template_name = 'silant_service/maintenance_form.html'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    template_name = 'silant_service/maintenance_confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')
