from django.urls import path, include
from .views import AlunosViewSet, CursoViewSet, MatriculaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursoViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")

urlpatterns = [
    path("", include(router.urls)),
]