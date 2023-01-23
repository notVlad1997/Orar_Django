from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, MaterieSerializer, AnSerializer, ZiSerializer, ProfesorSerializer, \
    GrupaSerializer, SalaSerializer, OrarSerializer
from .models import Materie, An, Grupa, Sala, Profesor, Zi, Orar
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {
        "name": "DJANGO"
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class MaterieViewSet(viewsets.ModelViewSet):
    queryset = Materie.objects.all()
    serializer_class = MaterieSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnViewSet(viewsets.ModelViewSet):
    queryset = An.objects.all()
    serializer_class = AnSerializer
    permission_classes = [permissions.IsAuthenticated]


class ZiViewSet(viewsets.ModelViewSet):
    queryset = Zi.objects.all()
    serializer_class = ZiSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GrupaViewSet(viewsets.ModelViewSet):
    queryset = Grupa.objects.all()
    serializer_class = GrupaSerializer
    permission_classes = [permissions.IsAuthenticated]


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrarViewSet(viewsets.ModelViewSet):
    queryset = Orar.objects.all()
    serializer_class = OrarSerializer

