from rest_framework import  serializers
from .models import Task, HealthBody, SocialRelationship, Travel, SchoolWork, Nature
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TaskSerializer(serializers.ModelSerializer):
        created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
        updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

        class Meta:
            model = Task
            fields = ['id', 'title', 'memo', 'created_at', 'updated_at']


class HealthBodySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = HealthBody
        fields = ['id', 'title', 'created_at', 'updated_at']

class SocialRelationshipSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = SocialRelationship
        fields = ['id', 'title', 'created_at', 'updated_at']

class TravelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Travel
        fields = ['id', 'title', 'created_at', 'updated_at']

class SchoolWorkSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = SchoolWork
        fields = ['id', 'title', 'created_at', 'updated_at']

class NatureSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Nature
        fields = ['id', 'title', 'created_at', 'updated_at']