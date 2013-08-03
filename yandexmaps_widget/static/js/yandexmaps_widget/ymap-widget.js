$(document).ready(function () {
    var placemark = null;

    ymaps.ready(function () {
        function gup(n,s){
            n = n.replace(/[\[]/,"\\[").replace(/[\]]/,"\\]");
            var p = (new RegExp("[\\?&]"+n+"=([^&#]*)")).exec(s);
            return (p===null) ? "" : p[1];
        }

        var scriptSrc = $('script[src*="ymap-widget.js"]').attr('src');
        var input_id = gup('input_id', scriptSrc);
        var center_latitude = gup('center_latitude', scriptSrc);
        var center_longitude = gup('center_longitude', scriptSrc);
        var default_zoom = gup('default_zoom', scriptSrc);

        function toPostgisPoint( geo_point ) {
            return ['POINT(',geo_point[0].toString(),geo_point[1].toString(),')'].join(' ');
        }

        function fillFromPostgisPoint(p) {
            var res = /POINT\s*\(\s*([0-9\.]+)\s*([0-9.]+)\s*\)/.exec(p),
            lat = parseFloat(res[1]),
            lng = parseFloat(res[2]);
            return [lat, lng];
        }

        $input = $('#' + input_id);

        function NewPlacemark(point) {
            var newPoint =  new ymaps.Placemark(
                point, {},
                {draggable: false, hasBalloon: false}
            );
            newPoint.events.add('dragend', function(e) {
                $input.val(toPostgisPoint(point));
            });
            return newPoint;
        }

        var center = [center_latitude, center_longitude];
        if($input.val())
            center = fillFromPostgisPoint($input.val());
        placemark = NewPlacemark(center);

        var map = new ymaps.Map("map", {
            zoom: default_zoom,
            center: center
        });
        map.geoObjects.add(placemark);
        map.controls.add("mapTools").add("zoomControl");

        map.events.add('click', function (e) {
            if(placemark) {
                map.geoObjects.remove(placemark);
                placemark.geometry.setCoordinates(e.get('coordPosition'));
            }
            else {
                placemark = NewPlacemark(e.get('coordPosition'));
            }
            map.geoObjects.add(placemark);
            $input.val(toPostgisPoint(placemark.geometry.getCoordinates()));
        });
    });
});