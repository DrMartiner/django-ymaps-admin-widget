# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.gis.db import models as gis


class Point(gis.Model):
    name = models.CharField(max_length=16)
    coords = gis.PointField()

    class Meta:
        verbose_name = 'point'
        verbose_name_plural = 'Points'

    def __unicode__(self):
        return self.name