from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Category(MPTTModel):
    """Модель(табличка) картегорий"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)
    description = models.TextField(verbose_name="Описание", max_length=1000, blank=True, default='')
    template = models.CharField(verbose_name="Шаблон", max_length=500, default='blog/Post.html')
    published = models.BooleanField(verbose_name="Отображать?", default=True)
    paginated = models.PositiveIntegerField(verbose_name='Количество новостей', default=0)
    sort = models.PositiveIntegerField("Порядок", default=0)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Teg(models.Model):
    """Модель тегов"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)
    published = models.BooleanField(verbose_name="Отображать?", default=True)

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
    published_date = models.DateTimeField(verbose_name="Дата публикации", default=timezone.now, blank=True, null=True)
    edit_date = models.DateTimeField(verbose_name="Дата редактирования", default=timezone.now, blank=True, null=True)
    image = models.ImageField(verbose_name="Главная фотография", upload_to="post/", blank=True, null=True)
    published = models.BooleanField(verbose_name="Отображать?", default=True)
    viewed = models.PositiveIntegerField(verbose_name="Просмотрено", default=0)
    status = models.BooleanField(verbose_name="Для зарегестрированых?", default=False)
    sort = models.PositiveIntegerField("Порядок", default=0)

    """Связи"""
    # set_null - при удалении не удаляется пост(cascade - удаляется), blank - обезательно ли поле, null - может ли быть пустым
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Teg, verbose_name='Тег', blank="True", )
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comment(models.Model):
    """Модель коментариев"""
    text = models.TextField(verbose_name="Текст", max_length=500)
    created_date = models.DateField(verbose_name="Дата", auto_now_add=True)
    moderation = models.BooleanField(verbose_name="Изменено", default=False)

    def __str__(self):
        return self.text

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
