from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Complaint

# Представления для модели Complaint (Рекламации)
class ComplaintListView(ListView):
    model = Complaint
    template_name = 'silant_service/complaint_list.html'

class ComplaintDetailView(DetailView):
    model = Complaint
    template_name = 'silant_service/complaint_detail.html'

class ComplaintCreateView(CreateView):
    model = Complaint
    fields = '__all__'
    template_name = 'silant_service/complaint_create.html'
    success_url = reverse_lazy('complaint_list')

class ComplaintUpdateView(UpdateView):
    model = Complaint
    fields = '__all__'
    template_name = 'silant_service/complaint_update.html'
    success_url = reverse_lazy('complaint_list')

class ComplaintDeleteView(DeleteView):
    model = Complaint
    template_name = 'silant_service/complaint_confirm_delete.html'
    success_url = reverse_lazy('complaint_list')