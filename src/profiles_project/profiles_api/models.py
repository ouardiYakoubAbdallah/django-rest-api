from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserProfileManager(BaseUserManager):
    """
        Helps Django to work with our custom user model.
    """

    def create_user(self, email, first_name , last_name, password=None):
        """
            Creates a new user profile object
        """
        if not email:
            raise ValueError('Users must have an email adress.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(self._db)

        return user

    def create_superuser(self, email, first_name , last_name, password):
        """
            Creates and saves a new superuser.
        """
        if not email:
            raise ValueError('Users must have an email adress.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True

        user.save(self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        Represents a user profile inside our system.
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """
            Used to get a users full name.
        """
        return self.first_name + self.last_name

    def get_short_name(self):
        """
            Used to get a users short name.
        """
        return self.first_name

    def __str__(self):
        return self.email

