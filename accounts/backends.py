# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class EmailBackend(ModelBackend):
#     """
#     Custom authentication backend that allows login with email instead of username
#     """
    
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # Try to get user by email (username field is actually email)
#             user = User.objects.get(email=username)
#         except User.DoesNotExist:
#             return None
        
#         # Check if password is correct
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
        
#         return None
    
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None