#coding=utf8
from django.db import models

# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=500)
    classify = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='goods_img/')
    inventory = models.IntegerField()
    price = models.FloatField()
    detail = models.CharField(max_length=1000)
    onsale_time = models.DateField()
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    deleted = models.IntegerField() #0代表未删除 1代表已删除

    class Meta: 
        ordering = ['-id']