# All urls local to api app
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view())
]