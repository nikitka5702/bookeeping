from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    class Meta:
        ordering = ['id']
        db_table = 'group'
        verbose_name_plural = 'Categories'

    INCOME = 'I'
    EXPENSE = 'E'

    CATEGORY_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense')
    ]

    name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=1, choices=CATEGORY_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BaseRecord(models.Model):
    class Meta:
        abstract = True

    account = models.ForeignKey('Account', models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)


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
