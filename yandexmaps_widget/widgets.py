# -*- coding: utf-8 -*-

from django.conf import settings
from django.forms import widgets
from django.template import loader


class YMapsPointWidget(widgets.Input):
    input_type = 'hidden'
    template = 'yandexmaps_widget/ymaps_point_widget.html'

    def __init__(self, *args, **kwargs):
        super(YMapsPointWidget, self).__init__(*args, **kwargs)

        # Define map options
        self.map_options = self.default_map_options
        extra_map_options = kwargs.get('map_options')
        if extra_map_options:
            self.map_options.update(extra_map_options)

    @property
    def default_map_options(self):
        return {
            'width': getattr(settings, 'YMAP_WIDTH', 600),
            'height': getattr(settings, 'YMAP_HEIGHT', 400),
            'zoom': getattr(settings, 'YMAP_ZOOM', 10),
            'latitude': getattr(settings, 'YMAP_CENTER_LATITUDE', 55.76),
            'longitude': getattr(settings, 'YMAP_CENTER_LONGITUDE', 37.64),
        }

    def render(self, name, value, attrs=None):
        r = super(YMapsPointWidget, self).render(name, value, attrs)
        params = self.map_options
        params['input_id'] = attrs['id']
        params['STATIC_URL'] = settings.STATIC_URL
        return r + loader.render_to_string(self.template, params)

    class Media(object):
        js = (
            "http://api-maps.yandex.ru/2.0-stable/?load=package.standard&lang=ru-RU",
            getattr(settings, 'YMAP_JQUERY_URL'),
        )