from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, *args, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        if not first_name:
            raise ValueError("Users must have a name")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.first_name = first_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, password=None, *args, **kwargs):
        user = self.create_user(email, first_name, password=password, **kwargs)

        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, *args, **kwargs):
        user = self.create_staffuser(email, first_name, password=password, **kwargs)

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        blank=False,
        unique=True,
    )

    first_name = models.CharField(max_length=150, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
