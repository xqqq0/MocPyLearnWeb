# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), default="female", max_length=10)
    address = models.CharField(max_length=100, verbose_name=u"地址", default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=100, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"忘记密码")), max_length=10)
    send_time = models.DateTimeField()