from django.db import models
from django.utils import timezone
from random import randint


class Client(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    citizenship = models.CharField(max_length=20, blank=False, default='Кыргызстан')
    birth_year = models.DateField(null=False, blank=False)
    work_place = models.CharField(max_length=30, null=True, blank=True)
    update_date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'Customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name} - {self.citizenship} - {self.birth_year}'


class Account(models.Model):
    number = models.CharField(max_length=16, null=False, blank=False, unique=True)
    account_type = models.IntegerField(default=1, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        db_table = 'Accounts'
        verbose_name = 'Акаунт'
        verbose_name_plural = 'Акаунты'

    def __str__(self):
        return f'{self.client.name}-{self.number}'


class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False)
    date = models.DateField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')

    class Meta:
        db_table = 'Loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return self.sum