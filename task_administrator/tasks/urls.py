from rest_framework import routers
from django.urls import path
#from .views.task_api_view import TaskViewSet, TaskAPIView, 
from .views.task_api_view import task_api_view, task_detail_api_view

#router = routers.DefaultRouter()

#router.register('api/tasks', TaskViewSet, 'tasks')

#urlpatterns = router.urls

#urlpatterns = [
#    path('apiview/', TaskAPIView.as_view(), name='task_api')
#]

urlpatterns = [
    path('apiview/', task_api_view, name='task_api'),
    path('apiview/<int:pk>/', task_detail_api_view, name='task_detail_api_view')
]