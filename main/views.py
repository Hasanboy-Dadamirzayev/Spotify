from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.generics import get_object_or_404

class SingerAPIView(APIView):
    def get(self, request):
        signers = Singer.objects.all()
        serializer = SingerSerializer(signers, many=True)
        response = {
            "Successfully": True,
            "data": serializer.data
        }
        return Response(response, status=HTTP_200_OK)

    def post(self, request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Successfully": True,
                "data": serializer.data
            }
            return Response(response, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class SignerRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        singer = get_object_or_404(Singer, id=pk)
        serializer = SingerSerializer(singer)
        response = {
            "Successfully": True,
            "data": serializer.data
        }
        return Response(response, status=HTTP_200_OK)

    def put(self, request, pk):
        singer = get_object_or_404(Singer, id=pk)
        serializer = SingerSerializer(singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Successfully": True,
                "data": serializer.data
            }
            return Response(response, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        singer = get_object_or_404(Singer, id=pk)
        singer.delete()
        response = {
            "data": "Singer deleted successfully"
        }
        return Response(response)

class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsTableSerializer(songs, many=True)
        response = {
            "Successfully": True,
            "data": serializer.data
        }
        return Response(response, status=HTTP_200_OK)

    def post(self, request):
        serializer = SongsTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Successfully": True,
                "data": serializer.data
            }
            return Response(response, status=HTTP_201_CREATED)
        return Response(serializer.errors)

