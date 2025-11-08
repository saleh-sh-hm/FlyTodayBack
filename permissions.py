from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsOwner(BasePermission):
    message = 'permissions denied'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.pk