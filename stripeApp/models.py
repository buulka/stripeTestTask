from django.db import models


class Discount(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'discounts'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'taxes'
        verbose_name_plural = 'Налоги'


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'orders'
        verbose_name_plural = 'Заказы'

