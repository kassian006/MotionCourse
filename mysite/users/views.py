from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class OwnerListAPIView(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerListSerializer


class OwnerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerDetailSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


