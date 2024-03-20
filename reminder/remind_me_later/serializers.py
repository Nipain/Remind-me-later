from rest_framework import serializers
from .models import Reminder

# creating serializers

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Reminder
        fields="__all__"
