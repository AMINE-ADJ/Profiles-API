from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        #In case of http method is put/patch/delete ( changing the objct en question),
        #we check if the authenticated user has permissions to modify the desired object in his request.
        return obj.id == request.user.id



    