from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Task
from todo.serializers import TaskSerializer


@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
