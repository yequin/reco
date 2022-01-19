from rest_framework.permissions import AllowAny


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def __init__(self, validate_owner=False):
        self.validate_owner = validate_owner

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False

    def has_object_permission(self, request, view, obj):
        # check if user who launched request is object owner
        if self.validate_owner:
            return bool(obj.person == request.user)
        return Truedjang