from django.db import models
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Page(models.Model):
    title = models.CharField(verbose_name="Имя ", max_length=100)
    text = models.TextField(verbose_name="Текст", max_length=100)
    sub_title = models.CharField(verbose_name="Подзаголовок", max_length=100, blank=True, null=True)
    edit_date = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True, blank=True, null=True)
    active = models.BooleanField(verbose_name="Показывать?", default=True)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)
    registration_required = models.BooleanField(verbose_name="Требуется регистрация", default=False)
    template = models.CharField(verbose_name="Шаблон", max_length=100, default='page/index.html')
    slug = models.SlugField(verbose_name="url", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
