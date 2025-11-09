from rest_framework import serializers
from .models import Ticket, Passenger, Booking

class CitySerializer(serializers.Serializer):
    CityName = serializers.CharField()

class TicketSerializer(serializers.ModelSerializer):
    origin = serializers.StringRelatedField(read_only = True)
    destination = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Ticket
        exclude = ['origin_airport','dest_airport','airplane_model','flight_law','price_detail','type',]

class TicketDetailSerializer(serializers.ModelSerializer):
    origin = serializers.StringRelatedField(read_only = True)
    destination = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Ticket
        exclude = ['type',]

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        exclude = ['id',]

class BookingSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = Booking
        fields = ['ticket', 'passengers']
        read_only_fields = ['ticket',]

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = Booking.objects.create(**validated_data)

        passengers = [Passenger(**data) for data in passengers_data]
        Passenger.objects.bulk_create(passengers,returning=True)
        booking.passengers.add(*passengers)

        booking.ticket.remaining_capacity -= len(passengers_data)
        booking.ticket.save()
        booking.save()
        return booking


class OrderSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(source='ticket.origin.CityName', read_only=True)
    destination = serializers.CharField(source='ticket.destination.CityName', read_only=True)
    date = serializers.DateField(source='ticket.date', read_only=True)
    depart_time = serializers.TimeField(source='ticket.depart_time', read_only=True)
    passenger_count = serializers.SerializerMethodField(read_only=True)
    tracking_number = serializers.CharField(read_only=True)

    class Meta:
        model = Booking
        fields = ['origin', 'destination', 'date', 'depart_time', 'passenger_count','tracking_number']

    def get_passenger_count(self, obj):
        return obj.passengers.count()