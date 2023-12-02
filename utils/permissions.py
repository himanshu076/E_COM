from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are not allowed to any request in some cases like "user-details",
        # so we'll dont allow GET, HEAD or OPTIONS requests.
        # breakpoint()
        if request.method in permissions.SAFE_METHODS:
            if obj == request.user:
                return True
            else:
                return False

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user
