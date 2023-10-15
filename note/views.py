from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer
from .models import Note


class NoteViewset(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()
