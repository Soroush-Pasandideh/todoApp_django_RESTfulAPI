from asyncio import tasks

from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('cats', views.CategoryViewSet)

urlpatterns = router.urls
