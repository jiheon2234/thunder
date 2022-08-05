from django.db import models
from django.contrib.auth.models import User
from goods.fields import ThumbnailImageField
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta

# 상품
class Goods (models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    is_new = models.BooleanField()
    can_change = models.BooleanField()
    where = models.TextField()
    image = ThumbnailImageField('IMAGE', upload_to='goods/%Y/%m')
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    already_sell = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods:goods_detail', args=self.id)

    @property
    def tts(self):
        time = timezone.now()-self.update_date
        if time<timedelta(minutes=1):
            return '방금 전'
        if time<timedelta(hours=1):
            return str(int(time.seconds/60))+'분 전'
        if time<timedelta(hours=7):
            return str(int(time.seconds/3600))+'시간 전'
        return '오래전'


class Comment (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    text = models.TextField(default='')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def tts(self):
        time = timezone.now() - self.update_date
        if time < timedelta(minutes=1):
            return '방금 전'
        if time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        return '오래전'





