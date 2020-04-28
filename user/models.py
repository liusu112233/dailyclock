from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField('姓名', max_length=30)
    age = models.IntegerField('年龄')
