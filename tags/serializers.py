from dataclasses import field
from inspect import ClosureVars
from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')