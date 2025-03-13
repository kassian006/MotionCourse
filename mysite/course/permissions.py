from rest_framework import permissions

class CheckEditOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class CheckStatusCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status=='owner':
            return True
        return False


class CheckStudentReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'student':
            return True
        return False
