from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, roles, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        for i in range(len(roles)):
            if roles[i] not in ["worker", "admin"]:
                raise ValueError("There is no such role")
        if not username:
            raise ValueError("Name is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, roles=roles, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, roles, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, roles, email, password, **extra_fields)

    def create_superuser(self, username, roles, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, roles, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=30)
    email = models.EmailField(_("email address"), unique=True)
    roles = ArrayField(models.CharField(_("roles"), max_length=20))

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user " "can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "roles"]

    def __str__(self):
        return self.email
