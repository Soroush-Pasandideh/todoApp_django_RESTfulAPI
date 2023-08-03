from django.contrib.auth import get_user_model
from rest_framework import serializers

from todo.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user = serializers.SlugRelatedField(read_only=True, default=serializers.CurrentUserDefault(), slug_field='username')
    user_id = serializers.IntegerField(read_only=True, source='user.id')

    class Meta:
        model = Task
        fields = ['id', 'user', 'user_id', 'title', 'description', 'completed', 'created_at', 'category']


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ['id', 'title', 'user']
