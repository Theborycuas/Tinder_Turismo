from django.test import tag
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Tag
from .serializers import TagSerializer

class TagListView(ListAPIView):
    serializer_class = TagSerializer
    permission_classes = ()
    queryset = Tag.objects.all()


class TagCreateView(CreateAPIView):
    serializer_class = TagSerializer
    permission_classes = ()


class TagRetriveView(RetrieveAPIView):
    serializer_class = TagSerializer
    permission_classes = ()
    queryset = Tag.objects.all()
    lookup_field = 'id'


class TagUpdateView(UpdateAPIView):
    serializer_class = TagSerializer
    permission_classes = ()
    queryset = Tag.objects.all()
    lookup_field = 'id'


class TagDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Tag.objects.all()
    lookup_field = 'id'
