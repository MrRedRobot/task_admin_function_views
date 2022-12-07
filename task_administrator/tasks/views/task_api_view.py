from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models.task import Task
from tasks.serializers.task_serializer import TaskSerializer, TestTaskSerializer

#class TaskViewSet(viewsets.ModelViewSet):
#    queryset = Task.objects.all()
#    permissions_classes = [permissions.AllowAny]
#    serializer_class = TaskSerializer

#class TaskAPIView(APIView):

 #   def get(self, request):
 #       tasks = Task.objects.all()
 #       task_serializer = TaskSerializer(tasks,many = True)
 #       return Response(task_serializer.data)

@api_view(['GET', 'POST'])
def  task_api_view(request):

    #list
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_serializer = TaskSerializer(tasks,many = True)

        return Response(task_serializer.data, status= status.HTTP_200_OK)

    #create
    elif request.method == 'POST':
        task_serializer = TaskSerializer(data = request.data)
        #validation
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({'message':'Tarea Creada Exitosamente!'}, status = status.HTTP_201_CREATED)
        return Response(task_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def task_detail_api_view(request,pk):
    #queryset
    task = Task.objects.filter(id = pk).first()
    if task:

        #retrieve
        if request.method == 'GET':
            task_serializer = TaskSerializer(task)
            return Response(task_serializer.data, status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            task_serializer = TestTaskSerializer(task,data= request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status = status.HTTP_200_OK)
            return Response(task_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        #delete
        elif request.method == 'DELETE':
            task.delete()
            return Response({'message':'Tarea Eliminada!'},status = status.HTTP_200_OK)

    return Response({'message':'TAREA NO ENCONTRADA!'},status = status.HTTP_400_BAD_REQUEST)
