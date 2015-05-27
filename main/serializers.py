__author__ = 'yangyangxinye'

from django.forms import widgets
from rest_framework import serializers
from main.models import Story, Poster, Location, Tag, TYPE_CHOICES


# class PosterSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=255)
#     points = serializers.IntegerField()
#
#
# class LocationSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     latitude = serializers.DecimalField(max_digits=20, decimal_places=10)
#     longitude = serializers.DecimalField(max_digits=20, decimal_places=10)
#     radius = serializers.IntegerField
#
#
# class Tag(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)


# class StorySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     type = serializers.ChoiceField(choices=TYPE_CHOICES, required=False)
#     title = serializers.CharField(max_length=140, required=False)
#     content = serializers.CharField(max_length=10000, required=False)
#     timestamp = serializers.DateTimeField(required=False)
#     originalPoster = serializers.PrimaryKeyRelatedField(queryset=Poster.objects.all(), required=False)
#     location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), required=False)
#     tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)
    # Need to set as blank somewhere for serializer.is_valid() to return True


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('id', 'type', 'title', 'content', 'timestamp', 'originalPoster', 'location', 'tags')

    def create(self, validated_data):
        """
        Create and return a new 'Story' instance, given the validated data
        """
        return Story.objects.create(validated_data)

    def update(self, instance, validated_data):
        """
        TODO: Update and return an existing 'Story' instance, given the validated data.
        """
        return instance



