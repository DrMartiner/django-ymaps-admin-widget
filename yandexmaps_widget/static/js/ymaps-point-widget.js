(function() {
  $(document).ready(function() {
    var placemark;
    placemark = null;
    return ymaps.ready(function() {
      var $input, NewPlacemark, center, convertPostGisToYandex, inputId, latitude, longitude, map, toPostgisPoint, zoom, _ref, _ref1, _ref2, _ref3;
      inputId = (_ref = window.inputId) != null ? _ref : 'id_coords';
      zoom = (_ref1 = window.zoom) != null ? _ref1 : 10;
      latitude = (_ref2 = window.latitude) != null ? _ref2 : '37.64';
      latitude = parseFloat(window.latitude.replace(',', '.'));
      longitude = (_ref3 = window.longitude) != null ? _ref3 : '37.64';
      longitude = parseFloat(window.longitude.replace(',', '.'));
      console.debug('Init params', latitude, longitude, zoom, inputId);
      toPostgisPoint = function(geo_point) {
        return ['POINT(', geo_point[1].toString(), geo_point[0].toString(), ')'].join(' ');
      };
      convertPostGisToYandex = function(point) {
        var coords;
        coords = /POINT\s*\(\s*([0-9\.]+)\s*([0-9.]+)\s*\)/.exec(point);
        if (coords.length !== 2) {
          console.error('Error at parse GIS point', point);
          return [];
        }
        return [parseFloat(coords[2]), parseFloat(coords[1])];
      };
      $input = $('#' + inputId);
      NewPlacemark = function(point) {
        var newPoint;
        newPoint = new ymaps.Placemark(point, {}, {
          draggable: false,
          hasBalloon: false
        });
        newPoint.events.add('dragend', function(e) {
          return $input.val(toPostgisPoint(point));
        });
        return newPoint;
      };
      center = [latitude, longitude];
      if ($input.val()) {
        center = convertPostGisToYandex($input.val());
      }
      placemark = NewPlacemark(center);
      console.debug('Init Yandex -> ', center);
      console.debug('Init PostGIS -> ', $input.val());
      map = new ymaps.Map("map", {
        zoom: zoom,
        center: center
      });
      map.geoObjects.add(placemark);
      map.controls.add('mapTools').add('zoomControl');
      return map.events.add('click', function(e) {
        if (placemark) {
          map.geoObjects.remove(placemark);
          placemark.geometry.setCoordinates(e.get('coordPosition'));
        } else {
          placemark = NewPlacemark(e.get('coordPosition'));
        }
        map.geoObjects.add(placemark);
        $input.val(toPostgisPoint(placemark.geometry.getCoordinates()));
        console.debug('');
        console.debug('Set Yandex -> ', e.get('coordPosition'));
        return console.debug('Set PostGIS -> ', $input.val());
      });
    });
  });

}).call(this);
