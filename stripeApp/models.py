from django.db import models


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

    class Meta:
        managed = True
        db_table = 'orders'
        verbose_name_plural = 'Заказы'
