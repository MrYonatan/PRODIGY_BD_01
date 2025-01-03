from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from uuid import uuid4

users = {}

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_id = str(uuid4())
        user_data = {**serializer.validated_data, "id":user_id}
        users[user_id] = user_data
        return Response(user_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_user(request, user_id):
    user = users.get(user_id)
    if not user:
        return Response({"error":"User not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(user, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user(request, user_id):
    user = users.get(user_id)
    if not user:
        return Response({"error":"User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(data=request.data, partial = True)
    if serializer.is_valid():
        updated_data = {**user, **serializer.validated_data}
        users[user_id] = updated_data
        return Response(updated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    if user_id not in users:
        return Response({"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)
    del users[user_id]
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET'])
def listUsersView(request):
    if not users:
        return Response({"error":"No User found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(users, status=status.HTTP_200_OK)