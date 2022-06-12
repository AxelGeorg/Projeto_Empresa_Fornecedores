from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("razaoSocial", "nomeFantasia", "cnpj", "endereco", "telefone",
                    "cidade", "uF", "nomeResponsavelLegal", "cpfResponsavelLegal")
