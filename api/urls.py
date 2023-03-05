from django.urls import path, include
from .views import AlunosViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers


router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursoViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")

urlpatterns = [
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAluno.as_view(), name="matriculas_aluno"),
    path("cursos/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view(), name="alunos_matriculados"),
]