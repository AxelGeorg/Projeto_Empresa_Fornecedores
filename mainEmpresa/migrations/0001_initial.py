# Generated by Django 4.0.4 on 2022-06-12 02:55

from django.db import migrations, models
import django_enum_choices.choice_builders
import django_enum_choices.fields
import mainEmpresa.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaoSocial', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('nomeFantasia', models.CharField(max_length=50, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=25, unique=True, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=80, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('uF', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'), ('Distrito Federal', 'Distrito Federal'), ('Espírito Santo', 'Espírito Santo'), ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'), ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'), ('Pará', 'Pará'), ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), ('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')], enum_class=mainEmpresa.models.EnumUF, max_length=19)),
                ('nomeResponsavelLegal', models.CharField(max_length=50, verbose_name='Nome Responsável Legal')),
                ('cpfResponsavelLegal', models.CharField(max_length=20, verbose_name='CPF Responsável Legal')),
            ],
        ),
    ]
