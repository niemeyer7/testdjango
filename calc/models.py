from django.db import models
from django.db.models.fields import AutoField, IntegerField

# Create your models here.

class dadospesquisa(models.Model):
    Fonte = models.CharField(max_length=200)
    Codigo = models.CharField(max_length=200)
    Descricao = models.CharField(max_length=2000)
    Unidade = models.CharField(max_length=200)
    Preco = models.DecimalField(decimal_places=2)


class Orcamento(models.Model):
    Fonte = models.CharField(max_length=200)
    Codigo = models.CharField(max_length=200)
    Descricao = models.CharField(max_length=2000)
    Unidade = models.CharField(max_length=200)
    Preco_Unit = models.DecimalField(decimal_places=2)
    Quantidade = models.TextField(blank=True, null=True)
    Preco = models.DecimalField(decimal_places=2, null=True)
    
#     class Meta:
#         db_table ="Nometabela" #Nome tabela

# class testesimples(models.Model):
#    title       = models.CharField(max_length=120) # max_length = required
#    description = models.TextField(blank=True, null=True)
#    price       = models.DecimalField(decimal_places=2, max_digits=10000)
#    summary     = models.TextField(blank=False, null=False)
#    featured    = models.BooleanField(default=False) # null=True, default=True