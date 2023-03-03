from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEl = (("B", "Básico"), ("I", "Intermediário"), ("A", "Avançado"))
    descricao = models.CharField(max_length=100)
    codigo_curso = models.CharField(max_length=10)
    nivel = models.CharField(max_length=1, choices=NIVEl, default="B", blank=False, null=False)

    def __str__(self):
        return self.descricao

