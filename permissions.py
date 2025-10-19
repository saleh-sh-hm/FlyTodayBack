from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsOwner(BasePermission):
    message = 'prmissions denied'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.pk
    
#     {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NTM0ODY2MSwiaWF0IjoxNzYwMTY0NjYxLCJqdGkiOiIwYzIxMjlkMzJjZjc0YzIxOWRlNDAzNmI4NTczYWUxMiIsInVzZXJfaWQiOiIxIn0.ND5R7UFoW2IlrF4KVtxNNSkaTIU-y_mtdD5wPRTxzkM",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1MzQ4NjYxLCJpYXQiOjE3NjAxNjQ2NjEsImp0aSI6IjYxYWI5ZDkzN2NiNzRjMTQ4MWFkYmZjZmQyNzY2Nzg2IiwidXNlcl9pZCI6IjEifQ.BJCSU5ZRZP5QOh0gs_I7b5ENVfUFIMTfPT-XPtdqMIQ"
# }