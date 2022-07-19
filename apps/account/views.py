from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.response import Response

from . import serializers


class RegisterView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.RegisterSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        # return super().get_queryset().filter(user=self.request.user)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)