from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializer import *

class ArtistModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['ism','davlat']
    ordering_fields = ['tugilgan_yil']



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


class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nom','janr']
    ordering_fields = ['davomiylik']
class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['sana']

    @action(detail=True,methods=['GET','POST'])
    def qoshiqlar(self,request,pk):
        if request.method == 'POST':
            qoshiq = request.data
            albom = self.get_object()
            serializer = QoshiqSerializer(data=qoshiq)
            if serializer.is_valid():
                serializer.save()
                oxirgi = Qoshiq.objects.last()
                albom.aktyorlar.add(oxirgi)
                albom.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        albom = self.get_object()
        qoshiqs = albom.qoshiq.all()
        serializer = QoshiqSerializer(qoshiqs,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





