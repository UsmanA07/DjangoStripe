from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='Укажите цену в целых числах, например, в копейках.'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_price_display(self):
        return f'{self.price // 100}'


class Order(models.Model):
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.items.name}'
