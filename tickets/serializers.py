from.models import *
from rest_framework import serializers

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields=['pk','reservation','name','mobile']
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
