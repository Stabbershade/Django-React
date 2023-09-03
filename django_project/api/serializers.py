from rest_framework import serializers
from .models import Room
# this file will translate the python code in models database into JSON format

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        #Match all the fields with the model. Id is the identification of the model
        fields = ('id','code','host','guest_can_pause','vote_to_skip','created_at')