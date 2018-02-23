# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Thirukural(models.Model):
    Kural_number = models.IntegerField(null = False)
    ChapterName = models.CharField(max_length = 30)
    Verse = models.TextField()
    
    class Meta:
        ordering = ['Kural_number']
    def __str__(self):
        return str(self.Kural_number)