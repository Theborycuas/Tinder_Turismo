from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import UserApp
from .serializers import UserSerializer

"""VER LISTA DE TODAS LAS CATEGORÍAS"""

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = ()
    queryset = UserApp.objects.all()

"""CREAR CATEGORÍAS DESDE LA API"""
class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()

"""LISTAR SEGUN ID"""

class UserRetriveView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = ()    
    queryset = UserApp.objects.all()
    lookup_field = 'id'

"""EDITA ELEMENTOS EN LA BASE DE DATOS"""
class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()    
    queryset = UserApp.objects.all()
    lookup_field = 'id'

"""ELIMINA ELEMENTOS EN LA BASE DE DATOS"""
class UserDestroyView(DestroyAPIView):
    permission_classes = ()    
    queryset = UserApp.objects.all()
    lookup_field = 'id'    
