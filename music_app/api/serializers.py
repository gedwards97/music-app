# Serializer will translate models to JSON response
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    # Model Meta (inner class of the model class)
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 
                  'votes_to_skip', 'created_at')


class CreateRoomSerializer(serializers.ModelSerializer):
   """
   Ensures that the data sent in POST request is valid.
   Corresponds with the fields required to create a room.
   """
   class Meta:
       model = Room
       fields = ('guest_can_pause', 'votes_to_skip') 
