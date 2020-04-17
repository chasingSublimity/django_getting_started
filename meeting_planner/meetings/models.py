from datetime import time
from django.db import models


class Room(models.Model):
  def __str__ (self):
    return f"{self.name}: room {self.room_number} on floor {self.floor_number}"

  name = models.CharField(max_length=150)
  floor_number = models.IntegerField(default=0)
  room_number = models.IntegerField(default=0)

class Meeting(models.Model):
  def __str__(self):
    return f"{self.title} at {self.start_time} on {self.date}"

  title = models.CharField(max_length=200)
  date = models.DateField()
  start_time = models.TimeField(default=time(9))
  duration = models.IntegerField(default=1)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)