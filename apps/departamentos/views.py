from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosEdit(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentosNovo(CreateView):
    model = Departamento
    fields = ['nome']


class DepartamentosDelete(DeleteView):
    model = Departamento