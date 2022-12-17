from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from codes.views import * # App_Views


class IsOwner(IsAuthenticated):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user.is_channel and request.user)
        return False

class PublicAvailable(IsAuthenticated):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user.is_channel in SAFE_METHODS or request.method in SAFE_METHODS)
        return False         

class IsAuthenticate(IsAuthenticated):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user or request.method in SAFE_METHODS)
        return False 
