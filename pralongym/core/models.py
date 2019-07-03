from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    #opções de sexo
    SEXO_CHOICES = [
        ["Feminino", "Feminino"],
        ["Masculino", "Masculino"],
        ["Trans", "Trans"],
        ["Gay", "Gay"],
        ["Bi","Bi"],
        ["Nao binario","Nao binario"],
        ["Outro","Outro"]
    ]

    #opções de avaliação de IMC
    AVALIACAO_CHOICES = [
        ["Menor que 18,5 - Abaixo do peso","Menor que 18,5 - Abaixo do peso"],
        ["Entre 18,5 e 24,9 - Peso Normal","Entre 18,5 e 24,9 - Peso Normal"],
        ["Entre 25 e 29,9 - Sobrepeso", "Entre 25 e 29,9 - Sobrepeso"],
        ["Entre 30 e 34,9 - Obesidade grau 1","Entre 30 e 34,9 - Obesidade grau 1"],
        ["Entre 35 e 39,9 - Obesidade grau 2","Entre 35 e 39,9 - Obesidade grau 2"],
        ["Mais do que 40 - Obesidade grau 3","Mais do que 40 - Obesidade grau 3"]
    ]

    #planos oferecidos pela academia
    PLANO_CHOICES = [
        ["1 modalidade - Bronze  R$60,00", "1 modalidade - Bronze  R$60,00"],
        ["2 modalidades - Prata R$100,00", "2 modalidades - Prata R$100,00"],
        ["3 modalidades - Ouro R$120,00", "3 modalidades - Ouro R$120,00"],
        ["Academia liberada - Diamante R$ de um rim", "Academia liberada - Diamante R$ de um rim"]
    ]

    #meta do cliente dentro da academia
    META_CHOICES = [
        ["Eliminar peso", "Eliminar peso"],
        ["Ganhar massa", "Ganhar massa"],
        ["Saude", "Saude"],
        ["Outro", "Outro"]
    ]

    nome = models.CharField(max_length = 50)
    sexo = models.TextField(max_length=50, choices=SEXO_CHOICES)
    data = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    imc = models.FloatField ()
    avaliacao = models.CharField(max_length = 50, choices=AVALIACAO_CHOICES)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length = 9, blank=True, null=True)
    plano = models.TextField(max_length=30 ,choices=PLANO_CHOICES)
    meta = models.TextField(max_length=30, choices=META_CHOICES) 
    ativo = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='cliente', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'cliente'