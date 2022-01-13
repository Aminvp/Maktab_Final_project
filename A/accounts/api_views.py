from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserListSerializer, UserUpdateSerializer, UserDetailSerializer, ProfileListSerializer, ProfileDetailSerializer, ProfileCreateSerializer, ProfileUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User, Profile
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserListSerializer(instance=users, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = UserRegisterSerializer(data=request.data)
        if data.is_valid():
            User.objects.create_user(email=data.validated_data['email'], full_name=data.validated_data['full_name'], password=data.validated_data['password']).save()
            return Response({'message': 'user registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'please enter your data (email, full_name, password) or enter to correct '}, status=status.HTTP_400_BAD_REQUEST)


# class UserLoginView(APIView):
#     def post(self, request):
#         data = UserLoginSerializer(data=request.data)
#         print('*' * 54)
#         if data.is_valid():
#             email = data.validated_data['email']
#             password = data.validated_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return Response({'messages': 'user login successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'email or password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserIdView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        srz_data = UserDetailSerializer(instance=user).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        srz_data = UserUpdateSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        profiles = Profile.objects.all()
        srz_data = ProfileListSerializer(instance=profiles, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        srz_data = ProfileCreateSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileIdView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        srz_data = ProfileDetailSerializer(instance=profile).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        self.check_object_permissions(request, profile)
        srz_data = ProfileUpdateSerializer(instance=profile, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer






