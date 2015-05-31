from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from main.models import Story
from main.serializers import StorySerializer


# Create your views here
class LocationStoryList(generics.ListAPIView):
    """ List all the stories given location details in 'GET'
    Want to have in the request: latitude, longitude, radius """
    serializer_class = StorySerializer

    def get(self, request, longitude, latitude, radius, format=None):
        stories = self.get_queryset(longitude, latitude, radius)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def get_queryset(self, longitude, latitude, radius):
        """ This view returns a list of all the stories for the given location """
        queryset = Story.objects.all()
        # Should actually check if either of them is None
        queryset = queryset.filter(
            location__latitude__gte=float(latitude)-float(radius), location__latitude__lte=float(latitude)+float(radius)
        ).filter(
            location__longitude__gte=float(longitude)-float(radius), location__longitude__lte=float(longitude)+float(radius)
        )
        return queryset


class StoryNew(APIView):
    def post(self, request, format=None):
        Story.create(request.data['type'], request.data['title'], request.data['content'])
        return Response('This is a POST request')


class StoryList(APIView):
    """
    List all the stories, or create a new one
    """
    def get(self, request, format=None):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
        # return Response("general for testing")

    def post(self, request, format=None):
        # Store the location information
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            story = serializer.save()
            story.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoryDetail(APIView):
    """
    Retrieve, update or delete a story instance
    """
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):

    # def delete(self, request, pk, format=None):

