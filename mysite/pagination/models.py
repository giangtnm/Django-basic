# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
