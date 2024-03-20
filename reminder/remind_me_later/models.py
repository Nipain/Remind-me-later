from django.db import models

# Creating reminder model.

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

