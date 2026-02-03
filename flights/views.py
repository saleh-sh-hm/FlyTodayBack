from django.utils import timezone
from rest_framework.response import Response
from rest_framework import generics,viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import City,Ticket,Booking
from .serializers import CitySerializer,TicketSerializer,TicketDetailSerializer,BookingSerializer,OrderSerializer
from .filters import TicketFilter,CityFilter


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter    
    # def get(self,request):
    #     names = City.objects.all()
    #     ser_data = CitySerializer(instance=names, many=True)
    #     return Response(data = ser_data.data)


class TicketView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filterset_class = TicketFilter
    
    serializer_action_classes = {
    'list': TicketSerializer,
    'retrieve': TicketDetailSerializer,
    'book_flight': BookingSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action,TicketSerializer)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def book_flight(self, request, pk=None):
        ticket = self.get_object()
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        passenger_count = len(serializer.validated_data['passengers'])

        if ticket.remaining_capacity < passenger_count:
            return Response('no capacity', status=status.HTTP_400_BAD_REQUEST)
        
        # now = timezone.localdate()
        # if ticket.date < now:
        #     return Response('ticket has expired', status=status.HTTP_400_BAD_REQUEST)

        booking = serializer.save(user=request.user, ticket=ticket)
        return Response("رزرو با موفقیت انجام شد", status=status.HTTP_201_CREATED)
        # return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)