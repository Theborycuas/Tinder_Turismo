from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import UserApp

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = '__all__'

    #Encripta las contraseñas al momento de Crear El usuario  
    def create(self, validated_data):
        user = UserApp(**validated_data)
        user.user_password = make_password(validated_data['user_password'])
        user.save()
        return user

    #Actualiza la contraseña de forma encriptadas
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.user_password = make_password(validated_data['user_password'])
        updated_user.save()
        return updated_user


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserApp

#     def to_representation(self, instance):
#         return {
#             'id': instance['id'],
#             'username': instance['username'],
#             'email': instance['user_email'],
#             'password': instance['user_password'],
#             'city': instance['city_id'],
#         }