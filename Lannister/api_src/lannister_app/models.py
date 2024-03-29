from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("Name is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, roles, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, roles, email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the Django authentication system are represented by this
    model.
    """

    username = models.CharField(_("username"), max_length=30)
    email = models.EmailField(_("email address"), unique=True)
    roles = ArrayField(models.CharField(_("roles"), max_length=20), default=["worker"])

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

    def __str__(self):
        return self.email


class Bonus_request(models.Model):
    class RequestStatus(models.TextChoices):
        CREATED = "Cr", _("Created")
        APPROVED = "Ap", _("Approved")
        REJECTED = "Rj", _("Rejected")
        DONE = "Dn", _("Done")

    creator = models.ForeignKey(User, related_name="creators", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        User, related_name="reviewers", null=True, blank=True, on_delete=models.SET_NULL
    )
    bonus_type = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=RequestStatus.choices,
        default=RequestStatus.CREATED,
    )

    class Meta:
        db_table = "bonus_request"

    def __repr__(self) -> str:
        return f"Creator id: {self.creator} - Bonus type: {self.bonus_type}"

    def __str__(self) -> str:
        return f"Creator id: {self.creator} - Bonus type: {self.bonus_type}"


class Bonus_request_history(models.Model):
    request_id = models.ForeignKey(Bonus_request, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    date_rejected = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    date_payment = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "bonus_request_history"

    def __repr__(self) -> str:
        return f"Request id: {self.request_id} - Creation date: {self.date_created}"

    def __str__(self) -> str:
        return f"Request id: {self.request_id} - Creation date: {self.date_created}"
