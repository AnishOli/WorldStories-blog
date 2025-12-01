from django.db import models
from  django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

#custom CustomerManager or Custom User model Manager because in built doesnot fullfill the requirements

class CustomManager(BaseUserManager):
    def create_user(self,email,password= None,**extra_fields):
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email) # checking the standard of email
        user = self.model(email= email, **extra_fields) 
        user.set_password(password)

        user.save(using = self._db) # saving data to database self._db
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

         # Validate that staff and superuser flags are True
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        # Call create_user to actually create the superuser
        return self.create_user(email, password, **extra_fields)
# Create your models here.
#custom user model
class Customer (AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True,max_length=200)
    phone_number = models.CharField(max_length=10, unique=True)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="",
        default='images/abc.jpg',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    objects = CustomManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
