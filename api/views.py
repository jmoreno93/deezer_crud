from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(["POST"])
@permission_classes([])
def login(request):
    if request.method == "POST":
        username = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            user_data = {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            return Response({"token": token.key, "user": user_data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(data={"message": "Logout successful"}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([])
def register_user(request):
    if request.method == "POST":
        fields = ["email", "password", "first_name", "last_name"]
        fields_error = []
        for field in fields:
            if field not in request.data:
                fields_error.append(field)

        if len(fields_error) > 0:
            return Response(data={"message": "Missing fields", "fields": fields_error},
                            status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get("email", None)
        password = request.data.get("password", None)
        email = username
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)

        if not username or not password or not first_name or not last_name:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            token = Token.objects.create(user=user)
            user_data = {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            return Response(data={"token": token.key, "user": user_data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"message": "Error creating user", "error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
