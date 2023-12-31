# import serializers from the REST framework
from rest_framework import serializers
 
# import the Guest data model
from .models import Guest, Booking, Review
 
# create a Guest serializer class
class GuestSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Guest
        fields = ('username','first_name','last_name')

# create a Booking serializer class
class BookingSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Booking
        fields = ('get_username','stay','check_in', 'check_out', 'number_guests')

# create a Review serializer class
class ReviewSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Review
        fields = ('get_username', 'rating', 'comment')