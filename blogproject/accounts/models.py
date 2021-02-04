# Django Imports
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

# My Project Imports
from .managers import CustomUserManager


# Article status constants
MASCULINO = "MASCULINO"
FEMININO = "FEMININO"
OUTROS = "OUTROS"
# CHOICES
GENDER_CHOICES = (
(MASCULINO, 'Masculino'),
(FEMININO, 'Feminino'),
(OUTROS, 'Outros'),
)


# Model for Custom User using AbstractBaseUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Access Info
    email = models.EmailField(_('email address'), unique=True)
    
    # User Info
    firstName = models.CharField(_('name'), max_length=100,blank=True, null=True)
    lastName = models.CharField(_('last name'), max_length=100,blank=True, null=True)
    gender = models.CharField(_('gender'), choices=GENDER_CHOICES,default='MASCULINO', max_length=100,blank=True, null=True)
    birthDate = models.DateField(_('birth date'), blank=True, null=True)
    image = models.ImageField(default='profile-pic-default.jpg',
                              upload_to='picprofile'
    )
    
    # Automatic filled Items
    joinedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # AbstractBaseUser Paramenters
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.firstName or self.lastName:
            return ("%s %s" % (self.firstName, self.lastName)).strip()
        return self.email

    class Meta:
        db_table = 'userData'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'



