from rest_framework import generics
from escola.models import Aluno, Curso
from .serializers import AlunoSerializer, CursoSerializer


class ALunoAPIView(generics.ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoAPIView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer