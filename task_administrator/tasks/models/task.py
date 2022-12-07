from django.db import models

STATE_CHOICES = [
    ('BACKLOG', 'Backlog'),
    ('TO DO', 'To Do'),
    ('DOING', 'Doing'),
    ('TEST', 'Test'),
    ('DONE', 'Done'),
]

PRIORITY_CHOICES = [
    ('ALTA', 'Alta'),
    ('MEDIA', 'Media'),
    ('BAJA', 'Baja'),
]

class Task(models.Model):
    name = models.CharField(max_length=100, null=False, unique = True)
    description = models.TextField(null=False)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, null=False)
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES, null=False)
    delivery_date = models.DateField(blank=True, null=False)

    def __str__(self):
        return self.name

    def getDeliveryDate(self):
        return self.delivery_date

    def save (self,*args,**kwargs):
        print(("SAVEEEEEE"))