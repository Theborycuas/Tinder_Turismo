from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Province
from .serializers import ProvinceSerializer

"""VER LISTA DE TODAS LAS CATEGORÍAS"""

class ProvinceListView(ListAPIView):
    serializer_class = ProvinceSerializer
    permission_classes = ()
    queryset = Province.objects.all()

"""CREAR CATEGORÍAS DESDE LA API"""
class ProvinceCreateView(CreateAPIView):
    serializer_class = ProvinceSerializer
    permission_classes = ()

"""LISTAR SEGUN ID"""

class ProvinceRetriveView(RetrieveAPIView):
    serializer_class = ProvinceSerializer
    permission_classes = ()    
    queryset = Province.objects.all()
    lookup_field = 'id'

"""EDITA ELEMENTOS EN LA BASE DE DATOS"""
class ProvinceUpdateView(UpdateAPIView):
    serializer_class = ProvinceSerializer
    permission_classes = ()    
    queryset = Province.objects.all()
    lookup_field = 'id'

"""ELIMINA ELEMENTOS EN LA BASE DE DATOS"""
class ProvinceDestroyView(DestroyAPIView):
    permission_classes = ()    
    queryset = Province.objects.all()
    lookup_field = 'id'    
