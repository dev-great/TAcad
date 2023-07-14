from rest_framework import generics
from .serializer import *
from .models import Work


class WorkCreate(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
