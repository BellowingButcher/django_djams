from django.shortcuts import render
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Songs, Artists
from .serializers import SongsSerializer, ArtistsSerializer
# Create views here.

class ArtistsAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return Artists.objects.get(pk=pk)
        except Artists.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArtistsSerializer(data)
        else:
            data = Artists.objects.all()
            serializer = ArtistsSerializer(data, many=True)
        
        return Response(serializer.data)

    # create artist
    def post(self, request, format=None):
        data = request.data
        serializer = ArtistsSerializer(data=data)
    # validate the data
        serializer.is_valid(raise_exception=True)
    # save the creation
        serializer.save()
    # inform front end of creation
        response = Response()
        response.data = {
            'message': 'Artist added successfully',
            'data': serializer.data
        }
        return response
    # update existing artist
    def put(self, request, pk=None, format=None):
        Artist_to_update = Artists.objects.get(pk=pk)
        data = request.data
        serializer = ArtistsSerializer(instance=Artist_to_update, data=data, partial=True)
        #validation
        serializer.is_valid(raise_exception=True)
        # save update
        serializer.save()
        # Inform the front end
        response = Response()
        response.data = {
            'message': 'Artist updated successfully',
            'data': serializer.data,
        }

        return response
    # delete artist
    def delete(self, request, pk, format=None):
        artist_to_delete = self.get_object(pk=pk)

        data = self.get_object(pk)
        serializer = ArtistsSerializer(data)

        response = Response()

        # inform the front end
        
        response.data = {
            'message': 'Deletion successful',
            'data': serializer.data,
        }

        artist_to_delete.delete()
        return response


# https://www.youtube.com/watch?v=x-0xWAJR3Fw This is the first video I watched to start building my viewset
class SongsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Songs.objects.get(pk=pk)
        except Songs.DoesNotExist:
            raise Http404

    
    # read operation for Songs
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongsSerializer(data)
        else:
            data = Songs.objects.all()
            serializer = SongsSerializer(data, many=True)

        return Response(serializer.data)

    # create operation for Songs
    def post(self, request, format=None):
        data = request.data
        serializer = SongsSerializer(data=data)

        # check if data is valid
        serializer.is_valid(raise_exception=True)

        # Save the Song
        serializer.save()

        # Inform front end of result
        response = Response()

        response.data = {
            'message': 'Song Created successfully',
            'data': serializer.data,
        }

        return response

    # def put()/patch() for updating songs
    def put(self, request, pk=None, format=None):
        song_to_update = Songs.objects.get(pk=pk)
        data = request.data
        serializer = SongsSerializer(instance=song_to_update, data=data, partial=True)

        #validation
        serializer.is_valid(raise_exception=True)

        # save update
        serializer.save()

        # Inform the front end
        response = Response()

        response.data = {
            'message': 'Song updated successfully',
            'data': serializer.data,
        }

        return response
    
    # def delete
    def delete(self, request, pk, format=None):
        song_to_delete = self.get_object(pk=pk)

        data = self.get_object(pk)
        serializer = SongsSerializer(data)

        response = Response()

        # inform the front end
        
        response.data = {
            'message': 'Deletion successful',
            'data': serializer.data,
        }

        song_to_delete.delete()
        return response