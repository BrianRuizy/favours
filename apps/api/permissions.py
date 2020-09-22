from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission grants, update, delete acces to owner
    """
    def has_object_permission(self, request, view, obj):
        # read allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions allowed for owner of post obj
        return obj.owner == request.user
