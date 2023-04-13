"""
Views for the recipe API.
"""
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    """
    Explanation notes:
    A viewset is a set of views, which represents a
    set of related functions or resources.
    The ModelViewSet class provides default implementations
    for CRUD (Create, Retrieve, Update, and Delete) operations.
    This means that the RecipeViewSet class will handle these
    operations automatically.
    """
    serializer_class = serializers.RecipeDetailSerializer
    # The queryset represent the objects that are available for this viewset.
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retrieve recipes for the authenticated use.
        We are overriding the get_queryset method, to add a filter
        by the user that is assigned to the request."""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Return the serializer class for the request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)


class TagViewSet(
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    """Manage tags in the database."""
    """
    The GenericViewSet does not automatically include CRUD operations.
    That is why we add them as user mixins.
    """
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
