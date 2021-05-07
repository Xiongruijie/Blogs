from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    name = models.CharField('名字', max_length=80)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.CharField('内容', max_length=10000)
    create_time = models.TimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('doc_blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])