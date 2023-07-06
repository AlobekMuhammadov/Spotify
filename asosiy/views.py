from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *

class ArtistlarAPIView(APIView):
    def get(self,request):
        artists = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(artists,many=True)
        return Response(serializer.data,status=status)


    def post(self,request):
        malumot = request.data
        serializer = QoshiqchiSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetail(APIView):
    def put(self,request,pk):
        key = Qoshiqchi.objects.get(id=pk)
        malumot = request.data
        serializer = QoshiqchiSerializer(malumot)
        if serializer.is_valid():
            key.update(serializer)
            key.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Qoshiqchi.objects.get(id=pk).delete()
        return Response(status=status.HTTP_100_CONTINUE)




