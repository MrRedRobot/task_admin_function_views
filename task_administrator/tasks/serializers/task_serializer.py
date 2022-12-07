import datetime

from django.utils import  timezone
from rest_framework import serializers
from tasks.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name','description','state', 'priority', 'delivery_date')
        read_only_fields = ('id',)

class TestTaskSerializer(serializers.Serializer):
    name = serializers.CharField()
    delivery_date = serializers.DateTimeField()

    def validate_name(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('Task name cannot be "admin"')
        return value

    def validate_delivery_date(self, value):
        if value == '':
            raise serializers.ValidationError('La fecha de entrega no puede ser nula')

        return value

    def validate(self, data):
        print("Validate general")
        return data

    def create(self,validate_data):
        print(validate_data)
        return Task.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.delivery_date = validate_data.get('delivery_date',instance.delivery_date)
        instance.save()
        return instance
