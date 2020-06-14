import uuid
import itertools
from autoslug import AutoSlugField
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, password=None):
        if not username:
            raise ValueError('User Must Be Have Username')
        user = self.model(
            username=username,
            full_name=full_name
        )
        user.username = username
        user.set_password(password)
        user.full_name = full_name
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password):
        user = self.create_user(
            username=username,
            password=password,
            full_name=full_name
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Username"), max_length=20, unique=True)
    full_name = models.CharField(_("Full Name"), max_length=50)
    last_login = models.DateField(_("Last Login"), auto_now_add=True)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', ]

    objects = CustomUserManager()


class Diary(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "Creator"), on_delete=models.DO_NOTHING)
    title = models.CharField(_("Title"), max_length=250, blank=True)
    diary = models.TextField(_("Diary"), blank=True)
    date = models.DateTimeField(_("Invented In"), auto_now_add=True)
    img = models.ImageField(_("Image (Optional)"), upload_to='image/diary',
                            height_field=None, width_field=None, max_length=None, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True, editable=True)

    class Meta:
        ordering = ('-date', )
        verbose_name = _("Diary")
        verbose_name_plural = _("Diarys")

    def __str__(self):
        return self.title

