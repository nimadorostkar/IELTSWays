from django.db import models
from accounts.models import User
from .utils import random_N_chars_str
from django.utils import timezone

class Invoice(models.Model):
    choices = (("پرداخت نشده", "پرداخت نشده"), ("پرداخت شده", "پرداخت شده"))
    status = models.CharField(max_length=15, default="پرداخت نشده", choices=choices)
    invoice_id = models.CharField(max_length=128, unique=True,blank=True,null=True)
    price = models.IntegerField(null=True, blank=True, verbose_name='مبلغ')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender",null=True, blank=True, verbose_name="کاربر فرستنده")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="توضیحات")
    file = models.FileField(null=True, blank=True, verbose_name='فایل فاکتور')
    due_date = models.DateField(verbose_name='تاریخ سررسید')
    created_at = models.DateField(auto_now_add=True,verbose_name='تاریخ صدور')
    pay_date = models.DateField(verbose_name='تاریخ پرداخت', null=True, blank=True)
    authority = models.CharField(max_length=36, null=True, blank=True)
    ref_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتور ها"
        managed = True

    def __str__(self):
        return str(self.invoice_id) + ' | ' + str(self.status)

