import re
import uuid as uuid
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,)
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, email, first_name, last_name, password, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, last_login=now,
                          date_joined=now, is_superuser=is_superuser, **extra_fields)

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, first_name=None, last_name=None, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, False, **extra_fields)

    def create_superuser(self, username, email, password):
        user = self._create_user(username, email, '', '', password, True)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    uu = models.UUIDField(unique=True, default=uuid.uuid4)
    username = models.CharField(_('username'), max_length=100, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      _('Enter a valid username.'), ('invalid'))])
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')