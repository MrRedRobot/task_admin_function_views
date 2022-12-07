from rest_framework import serializers
from tasks.models.comentary import Comentary

class ComentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentary
        fields = ('task','comentary_text')
        read_only_fields = ('id',)