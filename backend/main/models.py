from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    class Meta:
        db_table = 'group'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)


class BaseRecord(models.Model):
    class Meta:
        abstract = True

    account = models.ForeignKey('Account', models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Category, models.CASCADE)


class Account(models.Model):
    class Meta:
        db_table = 'account'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_open = models.DateField(null=True, blank=True)
    date_of_close = models.DateField(null=True, blank=True)
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    is_cash = models.BooleanField(default=False)


class Income(BaseRecord):
    class Meta:
        db_table = 'income'


class Expense(BaseRecord):
    class Meta:
        db_table = 'expense'

    cash_back = models.FloatField(default=0.0)
