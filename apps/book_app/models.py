# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
	title = models.TextField()
	author = models.CharField(max_length=255)
	published_date = models.DateField()
	category = models.CharField(max_length=255)
	in_print = models.BooleanField()
