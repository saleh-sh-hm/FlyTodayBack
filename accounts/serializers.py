from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    national_ID = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    telephone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email',
                  'national_ID','gender','nationality','birth_date','telephone','address')
        extra_kwargs = {
            'password':{'write_only' : True}
        }

    def validate_username(self,value):
        if len(value) != 11:
            raise serializers.ValidationError('phone must be 11 digits')
        if not value.isdigit():
            raise serializers.ValidationError('phone must contain only digits')
        return value
        