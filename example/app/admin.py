# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from yandexmaps_widget.widgets import YMapsPointWidget
from .models import Point


class PointAdminForm(forms.ModelForm):
    class Meta:
        model = Point
        widgets = {'coords': YMapsPointWidget()}


class PointAdmin(admin.ModelAdmin):
    form = PointAdminForm

admin.site.register(Point, PointAdmin)