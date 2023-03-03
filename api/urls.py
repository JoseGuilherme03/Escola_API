from django.urls import path
from .views import ALunoAPIView, CursoAPIView


urlpatterns = [
    path("alunos/", ALunoAPIView.as_view()),
    path("cursos/", CursoAPIView.as_view()),
]