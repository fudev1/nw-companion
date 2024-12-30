from rest_framework import serializers
from .models import TenantUser
from django.db import transaction

"""
    Serializer pour permettre aux users de créer leur compte via UI 
    Utilisation de REST Framework
"""


class TenantUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta: 
        model = TenantUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # @transaction.atomic
    # def create(self, validated_data): 
    #     user = TenantUser(
    #         last_name=validated_data['last_name'],
    #         first_name=validated_data['first_name'],
    #         email=validated_data['email']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=True)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()



class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    renew_paswword = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['renew_password']:
            raise serializers.ValidationError("Password must match !")
        return data