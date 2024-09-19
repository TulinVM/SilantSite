# accounts/views.py
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm  # Ваши кастомные формы

# Представление для регистрации пользователя
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm  # Форма для регистрации пользователя
    template_name = 'accounts/register.html'  # Шаблон для регистрации
    success_url = reverse_lazy('login')  # Перенаправление на страницу входа после успешной регистрации

    def form_valid(self, form):
        # Сохранение формы
        user = form.save()
        login(self.request, user)  # Выполняем автоматический вход после регистрации
        messages.success(self.request, 'Вы успешно зарегистрировались!')
        return redirect('home')  # Перенаправление на главную страницу

# Представление для входа пользователя
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  # Шаблон для входа
    authentication_form = AuthenticationForm  # Используемая форма для входа

    def form_invalid(self, form):
        messages.error(self.request, 'Неправильное имя пользователя или пароль.')
        return super().form_invalid(form)

# Представление для выхода пользователя
class UserLogoutView(LogoutView):
    template_name = 'silant_service/logout.html'  # Шаблон для выхода
    next_page = reverse_lazy('home')  # Перенаправление после выхода

# Представление для изменения профиля пользователя
class UserProfileUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm  # Ваша форма для изменения данных пользователя
    template_name = 'accounts/profile.html'  # Шаблон для изменения профиля
    success_url = reverse_lazy('profile')  # Перенаправление на страницу профиля после успешного изменения

    def get_object(self):
        # Возвращаем текущего пользователя
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Ваш профиль был успешно обновлен!')
        return super().form_valid(form)

# Представление для изменения пароля пользователя
class UserPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm  # Форма для изменения пароля
    template_name = 'accounts/password_change.html'  # Шаблон для изменения пароля
    success_url = reverse_lazy('profile')  # Перенаправление после изменения пароля

    def form_valid(self, form):
        messages.success(self.request, 'Ваш пароль был успешно изменен!')
        return super().form_valid(form)
