from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор поста', related_name="posts")
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Текст поста')

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return '{}'.format(self.title)
