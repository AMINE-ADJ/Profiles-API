from django.db import models
from  django.contrib.auth.models import AbstractBaseUser
from  django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manage the customized userPofile class so that "django (cli)" can use its functions to interact with our Customized class..create user..ect"""
     
    def create_user(self, email, name, password=None):
        """Create a new user profile """
        if not email : 
            raise ValueError('Users must ve email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password ):
        """Create superuser in our system"""
        user = self.create_user(email, name, password)

        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff=models.BooleanField(default = False )

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive full name of a user"""
        return self.name
    
    def get_short_name(self):
        """Retreive short name of user"""
        return self.name
    
    def __str__(self):
        """Return the string representation of our UserProfile object, recommended for all django models"""
        return self.email 