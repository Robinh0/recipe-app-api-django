"""
Serializers from recipe API.

Explanation of this module:
This Python code defines a serializer that takes information
about a recipe and returns it as JSON when the endpoint is called.

It packages and un-packages data, from and to the server.
We want to get a JSON version from de database and the model data.

"""
from rest_framework import serializers
from core.models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        # These are the fields that we want to convert from our model
        # (database) to our serializer.
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    # We are using the ModelSerializer because this serializer
    # is going to represent a specific model in the system,
    # and that is our recipe model.
    tags = TagSerializer(many=True, required=False)

    class Meta:
        # The Meta class is used to configure the serializer's behavior.
        # Here we are setting the model as the Recipe model.
        model = Recipe

        # These are the fields that are going to be returned by the API.
        fields = ['id', 'title', 'time_minutes', 'price', 'link', 'tags']
        # We don't want the user to change the database id of a recipe.
        # We only want them to be able to change the fields listed above.
        read_only_fields = ['id']

    # We are overriding the create method of the ModelSerializer.
    def create(self, validated_data):
        """Create a new recipe."""
        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(user=auth_user, **tag)
            recipe.tags.add(tag_obj)
        return recipe

    # Created with copilot, change if errors start occurring here. Lesson 102.
    def update(self, instance, validated_data):
        """Update a recipe."""
        tags = validated_data.pop('tags', [])
        recipe = super().update(instance, validated_data)
        recipe.tags.clear()
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(user=auth_user, **tag)
            recipe.tags.add(tag_obj)
        return recipe


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for the recipe details"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
