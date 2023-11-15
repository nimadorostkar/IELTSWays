from django.db import models
from accounts.models import User
from .utils import random_N_chars_str

class Letter(models.Model):
    letter_id = models.CharField(max_length=128, unique=True,blank=True,null=True)
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='عنوان')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    body = models.TextField(max_length=1000, null=True, blank=True, verbose_name="توضیحات")
    file = models.FileField(null=True, blank=True, verbose_name='فایل نامه')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "نامه"
        verbose_name_plural = "نامه ها"

    def __str__(self):
        return str(self.letter_id) + ' | ' + str(self.title)

