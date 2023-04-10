"""
Serializers from recipe API.

Explanation of this module:
This Python code defines a serializer that takes information
about a recipe and converts it into a format that can be
easily shared with other software systems.

The serializer will take specific information from a Recipe model
instance such as its ID, title, time in minutes to
prepare, price, and a link to a recipe page, and convert it into
a format that can be easily understood
by other systems.

For example, the serializer could convert the recipe information
into a JSON format that can be sent over the internet
and read by a web application or mobile device.
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    # We are using the ModelSerializer because this serializer
    # is going to represent a specific model in the system,
    # and that is our recipe model.

    class Meta:
        # The Meta class is used to configure the serializer's behavior.
        # Here we are setting the model as the Recipe model.
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        # We don't want the user to change the database id of a recipe.
        # We only want them to be able to change the fields listed above.
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for the recipe details"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
