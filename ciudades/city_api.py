from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import City
from .serializers import CitySerializer

"""VER LISTA DE TODAS LAS CATEGORÍAS"""

class CityListView(ListAPIView):
    serializer_class = CitySerializer
    permission_classes = ()
    queryset = City.objects.all()

"""CREAR CATEGORÍAS DESDE LA API"""
class CityCreateView(CreateAPIView):
    serializer_class = CitySerializer
    permission_classes = ()

"""LISTAR SEGUN ID"""

class CityRetriveView(RetrieveAPIView):
    serializer_class = CitySerializer
    permission_classes = ()    
    queryset = City.objects.all()
    lookup_field = 'id'

"""EDITA ELEMENTOS EN LA BASE DE DATOS"""
class CityUpdateView(UpdateAPIView):
    serializer_class = CitySerializer
    permission_classes = ()    
    queryset = City.objects.all()
    lookup_field = 'id'

"""ELIMINA ELEMENTOS EN LA BASE DE DATOS"""
class CityDestroyView(DestroyAPIView):
    permission_classes = ()    
    queryset = City.objects.all()
    lookup_field = 'id'    
