from django.db import models


class Category(models.Model):
    """Модель(табличка) картегорий"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"