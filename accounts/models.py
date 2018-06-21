from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.


class CustomUserManger(BaseUserManager):
    def create_user(self,email,firstname,lastname,auth_number,password):

        if not email:
            raise ValueError('Email is required')
        user = self.model( email = self.normalize_email(email),
                           firstname = firstname,
                           lastname = lastname,
                           auth_number = auth_number,)
        # TODO check to make sure password is encrypted with Bcrypt
        user.set_password(password)
        user.save(using=self._db)
        return user
    # COMPLETED create create_superuser here

    def create_superuser(self,email,firstname,lastname,auth_number,password):

        if not email:
            raise ValueError('Email is required')
        user = self.model( email = self.normalize_email(email),
                           firstname = firstname,
                           lastname = lastname,
                           auth_number = auth_number,)
        # TODO check to make sure password is encrypted with Bcrypt
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    auth_number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_authorized = models.BooleanField(default=False) # becomes True when user confirm Auth code

    objects = CustomUserManger()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','auth_number']

    """
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Review snippet below
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    """