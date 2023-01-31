from django.db import models
from django.contrib.auth.models import User


#Продукты в мазагизе (ассортимент)
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    description=models.TextField(blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    digital=models.BooleanField(default=False, null=True)
    image=models.ImageField(null=True, blank=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.name

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} {self.__class__.__name__}'