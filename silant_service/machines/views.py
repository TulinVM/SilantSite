# machines/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Machine
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView

# Главная страница с требованием аутентификации
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/login.html'  # Замените на ваш шаблон

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# Представления для модели Machine (Машина)
class MachineListView(ListView):
    model = Machine
    template_name = 'silant_service/machine_list.html'
    context_object_name = 'object_list'  # Имя контекста для использования в шаблоне

class MachineDetailView(DetailView):
    model = Machine
    template_name = 'silant_service/machine_detail.html'

class MachineCreateView(CreateView):
    model = Machine
    fields = '__all__'
    template_name = 'silant_service/machine_form.html'
    success_url = reverse_lazy('machine_list')

class MachineUpdateView(UpdateView):
    model = Machine
    fields = '__all__'
    template_name = 'silant_service/machine_update.html'
    success_url = reverse_lazy('machine_list')

class MachineDeleteView(DeleteView):
    model = Machine
    template_name = 'silant_service/machine_confirm_delete.html'
    success_url = reverse_lazy('machine_list')


# Представление для выхода пользователя
class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'  # Шаблон для выхода
    next_page = reverse_lazy('machine_list')  # Перенаправление после выхода


