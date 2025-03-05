from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import UserProfileSerializer, StudentListSerializer, OwnerListSerializer, UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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


