from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.models.user_manager import UserManager

class User(AbstractUser):
    username = None
    national_id = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "national_id"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return str(self.national_id)
