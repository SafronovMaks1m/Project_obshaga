from django.db import models
from django.utils import timezone
from django.urls import reverse

class Rooms(models.Model):
    number = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['number']

    def get_absolut_url_room(self):
        return reverse('obshaga:room',
                       args=[self.number])

    
class Sensors(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField()
    oxygen = models.FloatField()
    noise = models.FloatField()
    people = models.PositiveIntegerField()

    class Meta:
        ordering = ['time']

class Alert(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    sensor = models.CharField(max_length=11)
    value = models.FloatField()
    message = models.TextField()
    new = models.BooleanField(default=True)

    class Meta:
        ordering = ['time']

class TopViolators(models.Model):
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ['-quantity']