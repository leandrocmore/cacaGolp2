from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response   import Response
from rest_framework   import status
from .models import UserModels
from .serializer import UserSerializer

@api_view(['GET'])
def getUser(request):
    if request.method == 'GET':
        try:
            users = UserModels.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:

            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def userDetail(request):
    if request.method == 'GET':
        id_Gps = request.query_params.get('id_Gps')
        if id_Gps:
            try:
                user = UserModels.objects.get(pk=id_Gps)  # Corrigido para UserModels
                serialize = UserSerializer(user)
                return Response(serialize.data)
            except UserModels.DoesNotExist:  # Corrigido para UserModels
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id_Gps = request.query_params.get('id_Gps')
        try:
            update_user = UserModels.objects.get(pk=id_Gps)  # Corrigido para UserModels
        except UserModels.DoesNotExist:  # Corrigido para UserModels
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize = UserSerializer(update_user, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id_Gps = request.query_params.get('id_Gps')
        try:
            user_to_delete = UserModels.objects.get(pk=id_Gps)  # Corrigido para UserModels
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except UserModels.DoesNotExist:  # Corrigido para UserModels
            return Response(status=status.HTTP_404_NOT_FOUND)
