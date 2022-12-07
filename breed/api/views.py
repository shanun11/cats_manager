from rest_framework import viewsets

from .serializers import *
from breed.models import *

class BreedViewset(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()