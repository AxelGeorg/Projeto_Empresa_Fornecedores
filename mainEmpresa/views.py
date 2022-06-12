from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Empresa


class EmpresaList(ListView):
    model = Empresa


class EmpresaDetail(DetailView):
    model = Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('mainEmpresa:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tituloPagina"] = "Cadastrar"
        return context


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('mainEmpresa:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tituloPagina"] = "Editar"
        return context


class EmpresaDelete(DeleteView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('mainEmpresa:list')
