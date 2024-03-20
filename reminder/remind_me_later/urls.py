from django.contrib import admin
from django.urls import path,include
from .views import ReminderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reminder',ReminderViewSet )

urlpatterns = [
    path('', include(router.urls)),
]
