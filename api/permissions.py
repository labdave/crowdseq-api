from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.db.models import Q


class CanReleaseResultsPermission(permissions.BasePermission):
    message = 'Do not have permission to release analysis results.'

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        user = request.user
        has_permission = Permission.objects.filter((Q(group__user=user) | Q(user=user)) & Q(codename="release_results")).first()
        if has_permission:
            return True
        return False