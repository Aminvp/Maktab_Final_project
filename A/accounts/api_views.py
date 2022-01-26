from datetime import datetime

from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserRegisterSerializer, UserLoginSerializer, UserListSerializer, UserUpdateSerializer, \
    UserDetailSerializer, ProfileListSerializer, ProfileDetailSerializer, ProfileCreateSerializer, \
    ProfileUpdateSerializer, RequestOtpSerializer, RequestOtpResponseSerializer, VerifyOtpSerializer, \
    VerifyOtpResponseSerializer, RequestPhoneLoginSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User, Profile, OtpRequest
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers


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


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class OncePerMinuteThrottle(UserRateThrottle):
    rate = '1/minute'


class RequestOtp(APIView):
    throttle_classes = [OncePerMinuteThrottle]

    def post(self, request):
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            req_otp = OtpRequest()
            req_otp.phone = serializer.validated_data['phone']
            req_otp.channel = serializer.validated_data['channel']
            req_otp.generate_password()
            req_otp.save()
            # api = KavenegarAPI('467066542F7547496B7A2F34516745504D7173656E4934762F6F6243726B565A476F556B764D597A6F736F3D')
            # response = api.verify_lookup({
            #     'receptor': req_otp.phone,
            #     'token': req_otp.password,
            #     'template': settings.OTP_TEMPLATE
            # })
            # print(response)
            return Response(RequestOtpResponseSerializer(req_otp).data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            query = OtpRequest.objects.filter(
                request_id=serializer.validated_data['request_id'],
                phone=serializer.validated_data['phone'],
                valid_until__gte=datetime.now()
            )
            if query.exists():
                User = get_user_model()
                userq = User.objects.filter(email=serializer.validated_data['phone'])
                if userq.exists():
                    user = userq.first()
                    token, created = Token.objects.get_or_create(user=user)
                    return Response(data=VerifyOtpResponseSerializer({'token': token, 'new_user': False}).data)
                else:
                    user = User.objects.create(email=serializer.validated_data['phone'])
                    token, created = Token.objects.get_or_create(user=user)
                    return Response(data=VerifyOtpResponseSerializer({'token': token, 'new_user': True}).data)

            else:
                return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneLogin(APIView):
    def post(self, request):
        srz_data = RequestPhoneLoginSerializer(data=request.data)
        if srz_data.is_valid():
            query = User.objects.filter(
                phone=srz_data.validated_data['phone'],
                password=srz_data.validated_data['password'],
            )
            if query.exists():
                return Response(srz_data.data, status=status.HTTP_200_OK)
            else:
                return Response(srz_data.data, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(srz_data.errors, status=status.HTTP_401_UNAUTHORIZED)








