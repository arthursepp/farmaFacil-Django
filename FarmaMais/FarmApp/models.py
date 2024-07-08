from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default='emaildeexemplo@email.com')
    cpf = models.CharField(max_length=11)
    dataNasc = models.DateField()
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, null=True, blank=True, default='Not provided')
    cep = models.CharField(max_length=8)
    senha = (models.CharField(max_length=20))
    
    def __str__(self) -> str:
        return self.nome
    
class Farmacia(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()    
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=100)    
    senha = (models.CharField(max_length=20))   
    
    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    ean = models.CharField(max_length=13)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.CharField(max_length=5)
    dosagem = models.CharField(max_length=4)
    estoque = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nome