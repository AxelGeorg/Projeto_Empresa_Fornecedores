from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField


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


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=255, verbose_name="Razão Social")
    nomeFantasia = models.CharField(
        max_length=50, verbose_name="Nome Fantasia")
    cnpj = models.CharField(max_length=25, verbose_name="CNPJ", unique=True)
    endereco = models.CharField(max_length=80, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    uF = EnumChoiceField(EnumUF)
    nomeResponsavelLegal = models.CharField(
        max_length=50, verbose_name="Nome Responsável Legal")
    cpfResponsavelLegal = models.CharField(
        max_length=20, verbose_name="CPF Responsável Legal")

    def __str__(self) -> str:
        return self.razaoSocial
