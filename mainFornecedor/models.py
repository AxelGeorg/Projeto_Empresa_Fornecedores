from enum import Enum
from tabnanny import verbose
from django.db import models
from django_enum_choices.fields import EnumChoiceField

# Create your models here.


class EnumUF(Enum):
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapá"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceará"
    DF = "Distrito Federal"
    ES = "Espírito Santo"
    GO = "Goiás"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Pará"
    PB = "Paraíba"
    PR = "Paraná"
    PE = "Pernambuco"
    PI = "Piauí"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RJ = "Rio de Janeiro"
    RO = "Rondônia"
    RR = "Roraima"
    SC = "Santa Catarina"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"


class EnumCPFCNPJ(Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"


class Fornecedor(models.Model):

    nomeEmpresa = models.CharField(
        max_length=255, unique=True, verbose_name="Nome empresa")
    EhCPFCNPJ = EnumChoiceField(EnumCPFCNPJ)
    cnpj = models.CharField(
        max_length=25, verbose_name="CNPJ", unique=True, blank=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF", blank=True)
    rg = models.CharField(max_length=10, verbose_name="RG", blank=True)
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento", blank=True)
    endereco = models.CharField(max_length=80, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    uF = EnumChoiceField(EnumUF)
    pessoaContato = models.CharField(
        max_length=50, verbose_name="Pessoa Contato")
    dataHoraCadastro = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data e Hora Cadastro")
    dataHoraAlteracao = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Data e Hora Alteração")

    def __str__(self) -> str:
        return self.razaoSocial
