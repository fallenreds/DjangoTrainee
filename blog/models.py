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


class Teg(models.Model):
    """Модель тегов"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель Постов"""

    title = models.CharField(verbose_name="Заголовок", max_length=100)
    mini_text = models.TextField(verbose_name="Минитекст", max_length=100)
    text = models.TextField(verbose_name="Текст", max_length=1000)
    created_date = models.DateField(verbose_name="Дата", auto_now_add=True)
    slug = models.SlugField(verbose_name="url", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель коментариев"""
    text = models.TextField(verbose_name="Текст", max_length=500)
    created_date = models.DateField(verbose_name="Дата", auto_now_add=True)
    moderation = models.BooleanField(verbose_name="Изменено", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
