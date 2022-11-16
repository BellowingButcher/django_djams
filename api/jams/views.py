from django.shortcuts import render
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Songs
from .serializers import SongsSerializer
# Create your views here.

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

    # create operation