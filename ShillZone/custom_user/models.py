from django.db import models
import django
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    # function for user or superuser
    def _create_user(self, email, user_name, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # function for add normal user other field
    def create_user(self, email, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, user_name, password, **extra_fields)

    def create_superuser(self, email, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff = True.')
        if extra_fields.get('is_superuser' is not True):
            raise ValueError('Super user must have is_superuser = True')
        return self._create_user(email, user_name, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(ugettext_lazy('Email Address'), unique=True)
    user_name = models.CharField(ugettext_lazy('Username'), unique=True, max_length=250, blank=True, null=True,
                                 db_column="user_name")
    full_name = models.CharField(max_length=250, blank=True, null=True, db_column="full_name")
    phone_no = models.IntegerField(null=True)
    address = models.TextField(blank=True, null=True, db_column="address")
    otp = models.IntegerField(ugettext_lazy('OTP'), blank=True, null=True, db_column="otp")
    created_dt = models.DateTimeField(auto_now=True, db_column='Created Date')
    update_dt = models.DateTimeField(ugettext_lazy('Update Dt'), blank=True, null=True, db_column="update_dt")
    USERNAME_FIELD = 'email'  # set email as a username
    REQUIRED_FIELDS = ['user_name']

    objects = UserManager()

    def __str__(self):
        return self.email  # return value when call model as primary key

    #
    # def __init__(self):
    #     self.USERNAME_FIELD = request.COOKIES['username']

    class Meta:
        verbose_name_plural = "User_Info"  # display table name for admin
        db_table = 'User_Info'
