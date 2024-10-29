from rest_framework.permissions import BasePermission


class IsOrganizer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if obj.organizer == request.user:
                return True
        return False