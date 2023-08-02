from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

import core.models
from todo.filters import TaskFilter
from todo.models import Task, Category
from todo.serializers import TaskSerializer, CategorySerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'description', 'category__title']
    ordering_fields = ['title', 'completed', 'created_at']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()

        user_id = get_user_model().objects.only('id').get(pk=self.request.user.id)
        return Task.objects.filter(user_id=user_id)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
