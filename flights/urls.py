from django.urls import path
from . import views
from rest_framework import routers


app_name = 'flights'
urlpatterns = [
    path('city/', views.CityList.as_view(), name = 'city'),
    path('order/',views.OrderList.as_view(), name = 'order')
]

router = routers.SimpleRouter()
router.register('ticket',views.TicketView)
urlpatterns += router.urls

