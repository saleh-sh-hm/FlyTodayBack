from django_filters import rest_framework as filters
from .models import Ticket


class TicketFilter(filters.FilterSet):
    origin = filters.CharFilter(field_name='origin__CityName',lookup_expr='exact')
    destination = filters.CharFilter(field_name='destination__CityName',lookup_expr='exact')
    
    class Meta:
        model = Ticket
        fields = {
            'type' : ['exact'],
            'price' : ['gt','lt','range'],
                  }