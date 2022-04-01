from django.db import models
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Menu(models.Model):
    """Модель меню"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    is_auth = models.BooleanField(verbose_name="Для зарегестрированых?", default=False)
    active = models.BooleanField(verbose_name="Показывать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItems(MPTTModel):
    name = models.CharField(verbose_name="Имя латиница", max_length=100)
    title = models.CharField(verbose_name="Имя русский", max_length=100)
    parent = TreeForeignKey('self', verbose_name="Родительская категория", on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    menu = models.ForeignKey(Menu, verbose_name='Меню', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(verbose_name="Статус", default=True)
    is_auth = models.BooleanField(verbose_name="Для зарегестрированых?", default=False)
    anchor = models.CharField(verbose_name="Якорь", max_length=100)
    url = models.SlugField(verbose_name="url", max_length=100)
    active = models.BooleanField(verbose_name="Показывать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПодМеню"
        verbose_name_plural = "ПодМеню"
