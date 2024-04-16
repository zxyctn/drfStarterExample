from backend.api.models import Car
from rest_framework import viewsets

from backend.api.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cars to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
