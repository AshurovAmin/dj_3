from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, verbose_name='Гражданство', default='Кыргызстан')
    birth_year = models.DateField(verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, verbose_name='Место работы', blank=True, null=True)
    update_date = models.DateField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateField(auto_now_add=True, verbose_name='Дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Счет')

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


