from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название (текущий или архивный)')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Box(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог', related_name='box')
    name = models.CharField(max_length=40, verbose_name='Название')
    photo = models.ImageField(upload_to='girafic_app/img', verbose_name='Фото')
    description = models.CharField(max_length=100, verbose_name='Описание')
    lenght = models.FloatField(verbose_name='Длина, см')
    width = models.FloatField(verbose_name='Ширина, см')
    height = models.FloatField(verbose_name='Высота, см')
    cost = models.IntegerField(verbose_name='Цена, руб.')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)

    def __str__(self):
        return 'Праздничная коробка "' + str(self.name) + '"'

    class Meta:
        verbose_name = 'Коробка'
        verbose_name_plural = 'Коробки'

class Dreamcatcher(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог', related_name='dreamcatcher')
    name = models.CharField(max_length=40, verbose_name='Название')
    photo = models.ImageField(upload_to='girafic_app/img', verbose_name='Фото')
    description = models.CharField(max_length=100, verbose_name='Описание')
    diameter = models.FloatField(verbose_name='Длина, см')
    cost = models.IntegerField(verbose_name='Цена, руб.')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Ловец снов'
        verbose_name_plural = 'Ловцы снов'

class Letter(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог', related_name='letter')
    name = models.CharField(max_length=40, verbose_name='Название')
    photo = models.ImageField(upload_to='girafic_app/img', verbose_name='Фото')
    description = models.CharField(max_length=100, verbose_name='Описание')
    lenght = models.FloatField(verbose_name='Длина, см')
    width = models.FloatField(verbose_name='Ширина, см')
    color = models.CharField(max_length=40, choices=[('Белый','Белый'),('Крафтовый','Крафтовый')], verbose_name='Цвет')
    cost = models.IntegerField(verbose_name='Цена, руб.')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Конверт'
        verbose_name_plural = 'Конверты'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True)
    text = models.TextField(verbose_name='Отзыв')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True, related_name='order')
    ready = models.BooleanField(verbose_name='выполнен', default=False, blank=True)

    @classmethod
    def create(cls, user, ready=False):
        order = cls(user=user, ready=ready)
        return order

    def __str__(self):
        return 'Заказ №'+str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ClientData(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, verbose_name='Заказ', related_name='order', null=True)
    fullname = models.CharField(max_length=150, verbose_name='Фамилия, Имя, Очество')
    post_address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    class Meta:
        verbose_name = 'Клиент дата'

class BoxOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, verbose_name='Заказ', related_name='order_with_box', null=True)
    lenght = models.FloatField(verbose_name='Длина, см', blank=True)
    width = models.FloatField(verbose_name='Ширина, см', blank=True)
    height = models.FloatField(verbose_name='Высота, см', blank=True)
    name = models.CharField(verbose_name='Название', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name = 'Заказ коробок'
        verbose_name_plural = 'Заказы коробок'

class DreamcatcherOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, verbose_name='Заказ', related_name='order_with_dreamcatcher', null=True)
    diameter = models.FloatField(verbose_name='Длина, см', blank=True)
    name = models.CharField(verbose_name='Название', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name = 'Заказ ловцов снов'
        verbose_name_plural = 'Заказы ловцов снов'

class LetterOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, verbose_name='Заказ', related_name='order_with_letter', null=True)
    lenght = models.FloatField(verbose_name='Длина, см', blank=True)
    width = models.FloatField(verbose_name='Ширина, см', blank=True)
    color = models.CharField(max_length=40, choices=[('Белый','Белый'),('Крафтовый','Крафтовый')], verbose_name='Цвет', blank=True)
    name = models.CharField(verbose_name='Название', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name = 'Заказ письма'
        verbose_name_plural = 'Заказы писем'

