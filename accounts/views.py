from .serializers import UserSerializer
from accounts.models import User
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from permissions import IsOwner

class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin):
    permission_classes = [IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data, password=password)
        serializer.instance = user

    def perform_update(self, serializer):
        user = serializer.save()
        password = self.request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
    

# class UserRegister(APIView):
#     def post(self,request):
#         ser_data = UserSerializer(data = request.POST)
#         if ser_data.is_valid():
#             User.objects.create_user(
#                 username=ser_data.validated_data['username'],
#                 password=ser_data.validated_data['password']
#             )
#             return Response("user created")
#         return Response(ser_data.errors)
#
#     def get(self,request):
#         users = User.objects.all()
#         ser_data = UserSerializer(instance=users, many=True)
#         return Response(data=ser_data.data)
#
#     def put(self,request,pk):
#         pass


    # def list(self,request):
    #     Response({'test':'hello'})
    # def create(self,request):
    #     Response('hello')
    # def retrieve(self,request,pk=None):
    #     pass
    # def partial_update(self,request,pk=None):
    #     pass