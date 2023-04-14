"""
URL mappings for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

# We can use the DefaultRouter with an APIView,
# to automatically create routes for all of the different options
# available for that view.
router = DefaultRouter()

# This creates a new endpoint, api/recipes and it will
# assign all of the different endpoints from our recipe
# viewset to that endpoint. Because we are using the
# ModelViewset, its going to include all CRUD operations and
# endpoints (GET, POST, PUT, PATCH, DELETE).
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
