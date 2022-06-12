from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date
from datetime import datetime

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor


class FornecedorList(ListView):
    model = Fornecedor
    fields = '__all__'

    def get_queryset(self):

        txtNomeEmpresa = self.request.GET.get('nomeEmpresa')
        if txtNomeEmpresa:
            return Fornecedor.objects.filter(
                nomeEmpresa__icontains=txtNomeEmpresa)

        txtCPF = self.request.GET.get('cpf')
        if txtCPF:
            return Fornecedor.objects.filter(
                cpf__icontains=txtCPF)

        txtCNPJ = self.request.GET.get('cnpj')
        if txtCNPJ:
            return Fornecedor.objects.filter(
                cnpj__icontains=txtCNPJ)

        return Fornecedor.objects.all()


class FornecedorDetail(DetailView):
    model = Fornecedor
    fields = '__all__'


def verificar_data(data):
    if data:
        data = datetime.strptime(data, "%d/%m/%Y")
        today = date.today()
        if (today.year - data.year - ((today.month, today.day) < (data.month, data.day))) >= 18:
            return True
        else:
            return False

    return True


class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = '__all__'
    success_url = reverse_lazy('mainFornecedor:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tituloPagina"] = "Cadastrar"
        return context

    def form_valid(self, form):
        if verificar_data(form.data['data_nascimento']) == False:
            form.add_error('data_nascimento', ValidationError(
                f"Fornecedor não pode ser menor de idade."))
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = '__all__'
    success_url = reverse_lazy('mainFornecedor:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tituloPagina"] = "Editar"
        return context

    def form_valid(self, form):
        if verificar_data(form.data['data_nascimento']) == False:
            form.add_error('data_nascimento', ValidationError(
                f"Fornecedor não pode ser menor de idade."))
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


class FornecedorDelete(DeleteView):
    model = Fornecedor
    fields = '__all__'
    success_url = reverse_lazy('mainFornecedor:list')
