from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Category
from .serializers import CategorySerializer

"""VER LISTA DE TODAS LAS CATEGORÍAS"""

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = ()
    queryset = Category.objects.all()

"""CREAR CATEGORÍAS DESDE LA API"""
class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = ()

"""LISTAR SEGUN ID"""

class CategoryRetriveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = ()    
    queryset = Category.objects.all()
    lookup_field = 'id'

"""EDITA ELEMENTOS EN LA BASE DE DATOS"""
class CategoryUpdateView(UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = ()    
    queryset = Category.objects.all()
    lookup_field = 'id'

"""ELIMINA ELEMENTOS EN LA BASE DE DATOS"""
class CategoryDestroyView(DestroyAPIView):
    permission_classes = ()    
    queryset = Category.objects.all()
    lookup_field = 'id'    
