from django.shortcuts import render
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Songs, Artists, Managers
from .serializers import SongsSerializer, ArtistsSerializer, ManagersSerializer
from rest_framework import status, generics
# Create views here.

# refactoring views to use mixins generic views 
# this class is specifically for reading, creating, and updating functionality
class ManagersList(generics.ListCreateAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer


class ManagersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer

# managers crud functionality done
# class ManagersAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Managers.objects.get(pk=pk)
#         except Managers.DoesNotExist:
#             raise Http404

#     def get(self, request, format=None):
#         managers = Managers.objects.all()
#         serializer = ManagersSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ManagersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         manager = self.get_object(pk)
#         serializer = ManagersSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         manager = self.get_object(pk)
#         manager.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# artist viewset
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