from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import UserProfileSerializer, StudentListSerializer, OwnerListSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class OwnerListAPIView(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerListSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


