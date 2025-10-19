from rest_framework.response import Response
from .models import City,Ticket,Booking
from .serializers import CitySerializer,TicketSerializer,TicketDetailSerializer,BookingSerializer,OrderSerializer
from rest_framework import generics,viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .filters import TicketFilter



class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer    
    # def get(self,request):
    #     names = City.objects.all()
    #     ser_data = CitySerializer(instance=names, many=True)
    #     return Response(data = ser_data.data)


class TicketView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Ticket.objects.all()
    filterset_class = TicketFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TicketSerializer
        if self.action == 'retrieve':
            return TicketDetailSerializer    
        if self.action == 'book_flight':
            return BookingSerializer
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def book_flight(self, request, pk=None):
        ticket = self.get_object()
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        passenger_count = len(serializer.validated_data['passengers'])

        if ticket.remaining_capacity < passenger_count:
            return Response('no capacity', status=status.HTTP_400_BAD_REQUEST)

        booking = serializer.save(user=request.user, ticket=ticket)
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)