from .models import User, Profile, OtpRequest
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserListSerializer(serializers.ModelSerializer):
    # store = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    # def get_store(self, obj):
    #     result = obj.store.get()
    #     return StoreSerializer(instance=result).data


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'objects')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


class RequestOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, allow_null=False)
    channel = serializers.ChoiceField(allow_null=False, choices=['android', 'ios', 'web'])


class RequestOtpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['request_id']


class VerifyOtpSerializer(serializers.Serializer):
    request_id = serializers.CharField(max_length=64, allow_null=False)
    phone = serializers.CharField(max_length=12, allow_null=False)
    password = serializers.CharField(allow_null=False)


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_user = serializers.BooleanField()


class RequestPhoneLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, allow_null=False)
    password = serializers.CharField()


















