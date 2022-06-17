from django.contrib.auth.models import User
from rest_framework import serializers

class UserShortSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()

class UserSerializer(UserShortSerializer):
    password = serializers.CharField()
    is_staff = serializers.BooleanField(default= False)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.username = validated_data.get('username')
        instance.is_staff = validated_data.get('is_staff')
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
