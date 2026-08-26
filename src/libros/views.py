from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from .models import Libros
from .serializer import LibrosSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def libros(request):
    if request.method == 'GET':
        libros = Libros.objects.all()
        serializer = LibrosSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = LibrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Libro creado'}, status=status.HTTP_201_CREATED)
        return Response({'mensaje':'No se pudo cargar el libro'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def libros_detail(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    if request.method == 'GET':
        serializer = LibrosSerializer(libro)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = LibrosSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Se edito el libreo'},status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        libro.delete()
        return Response({'mensaje':'Se elimino el libro'}, status=status.HTTP_200_OK)