from rest_framework import viewsets, generics, status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import (VerifyResetCodeSerializer,
    UserSerializer,
    LoginSerializer,
    LogoutSerializer,
    UserProfileSerializer,
    UserProfileSimpleSerializer,
    StudentListSerializer,
    StudentsSerializer,
    StudentEditSerializer,
    CartCreateSerializer,
    CartSerializer,
    CartItemCreateSerializer,
    CartItemSerializer,
    OwnerListSerializer,
    OwnerDetailSerializer,
    GroupSerializer,
    GroupSimpleSerializer,
    GroupMemberSerializer,
    GroupMemberSimpleSerializer,
    MessageSerializer,
    GroupDetailSerializer,
    UserProfileListSerializers
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework import viewsets, filters
from rest_framework.generics import RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from course.permissions import CheckEditOwner, CheckStudentReview


@api_view(['POST'])
def verify_reset_code(request):
    serializer = VerifyResetCodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    serializer_class = LogoutSerializer  # Указываем сериализатор

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

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class StudentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartItemListAPIView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartItemCreateAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)


class OwnerListAPIView(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['courses__status']  # Указываем правильное поле
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        queryset = Owner.objects.all()
        filter_type = self.request.query_params.get('type')

        if filter_type == 'free':
            queryset = queryset.filter(courses__status='free').distinct()
        elif filter_type == 'paid':
            queryset = queryset.filter(courses__status='paid').distinct()

        return queryset


class OwnerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerDetailSerializer
    lookup_field = "pk"
    # permission_classes = [CheckEditOwner]

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)



class AllStudentsAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['courses__status']
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        queryset = Student.objects.all()
        filter_type = self.request.query_params.get('type')

        if filter_type == 'free':
            queryset = queryset.filter(courses__status='free').distinct()
        elif filter_type == 'paid':
            queryset = queryset.filter(courses__status='paid').distinct()

        return queryset


class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Устанавливаем текущего пользователя как автора


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Устанавливаем текущего пользователя как автора


class GroupMemberView(generics.ListCreateAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Устанавливаем текущего пользователя как автора


class GroupMemberRetrieve(generics.RetrieveDestroyAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Устанавливаем текущего пользователя как автора


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """Переопределяем метод создания, чтобы проверить членство в группе"""
        user = self.request.user
        group = serializer.validated_data['group']  # Получаем группу из запроса

        # Проверяем, состоит ли пользователь в группе
        if not GroupMember.objects.filter(group=group, users=user).exists():
            return Response(
                {"detail": "Вы не состоите в этой группе."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Если все ок — сохраняем сообщение
        serializer.save(author=user)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """Переопределяем метод создания, чтобы проверить членство в группе"""
        user = self.request.user
        group = serializer.validated_data['group']  # Получаем группу из запроса

        # Проверяем, состоит ли пользователь в группе
        if not GroupMember.objects.filter(group=group, users=user).exists():
            return Response(
                {"detail": "Вы не состоите в этой группе."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Если все ок — сохраняем сообщение
        serializer.save(author=user)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Group, GroupMember
from django.contrib.auth import get_user_model


class RemoveUserFromGroupView(APIView):
    def delete(self, request, group_id, user_id):
        # Получаем объект группы
        group = get_object_or_404(Group, id=group_id)

        # Получаем объект пользователя
        user = get_object_or_404(get_user_model(), id=user_id)

        # Получаем объект GroupMember для этой группы
        group_member = get_object_or_404(GroupMember, group=group)

        # Проверяем, состоит ли пользователь в группе
        if user not in group_member.users.all():
            return Response(
                {"detail": f"User {user.username} is not a member of the group."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Удаляем пользователя из группы
        group_member.users.remove(user)

        return Response(
            {"detail": f"User {user.username} has been removed from the group {group.room_group_name}."},
            status=status.HTTP_200_OK
        )
