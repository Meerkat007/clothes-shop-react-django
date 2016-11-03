from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255, db_index=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_('Date of Birth'))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now, verbose_name=_('Date Joined'))

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name + self.last_name)

    def get_short_name(self):
        return self.first_name
