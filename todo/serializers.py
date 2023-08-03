from django.contrib.auth import get_user_model
from rest_framework import serializers

from todo.models import Task, Category
from todoApp_django_RESTfulAPI.settings import AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class TaskSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, default=serializers.CurrentUserDefault(),
    #                                     slug_field='username/')
    # user_id = serializers.IntegerField(read_only=True, source='user.id')
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'completed', 'created_at', 'category']


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ['id', 'title', 'user']
