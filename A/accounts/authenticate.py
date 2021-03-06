from .models import User, Profile


class PhoneBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(phone=email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None