from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'completed', 'created_at', 'category']
