from django.contrib import admin
from .models import Aluno, Curso, Matricula


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "rg", "cpf", "data_nascimento")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "codigo_curso", "nivel")
    list_display_links = ("id", "codigo_curso")
    search_fields = ("codigo_curso",)
    list_per_page = 20


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "periodo",)
    list_display_links = ("id",)
    list_per_page = 20


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
