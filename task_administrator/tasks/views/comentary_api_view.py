from rest_framework import viewsets, permissions
from tasks.models import Comentary
from tasks.serializers import ComentarySerializer

class ComentaryViewSet(viewsets.ModelViewSet):
    queryset = Comentary.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ComentarySerializer