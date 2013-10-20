$(document).ready () ->
    placemark = null

    ymaps.ready () ->
        inputId = window.inputId ? 'id_coords'

        zoom = window.zoom ? 10

        latitude = window.latitude ? '37.64'
        latitude = parseFloat window.latitude.replace(',', '.')

        longitude = window.longitude ? '37.64'
        longitude = parseFloat window.longitude.replace(',', '.')

        console.debug 'Init params', latitude, longitude, zoom, inputId

        toPostgisPoint = (geo_point) ->
            return ['POINT(',geo_point[0].toString(),geo_point[1].toString(),')'].join(' ')

        fillFromPostgisPoint = (p) ->
            res = /POINT\s*\(\s*([0-9\.]+)\s*([0-9.]+)\s*\)/.exec p
            lat = parseFloat res[1]
            lng = parseFloat res[2]
            return [lat, lng]

        $input = $('#' + inputId)

        NewPlacemark = (point) ->
            newPoint =  new ymaps.Placemark point, {},
                draggable: false
                hasBalloon: false
            newPoint.events.add 'dragend', (e) ->
                $input.val toPostgisPoint(point)
            return newPoint

        center = [latitude, longitude]
        if $input.val()
            center = fillFromPostgisPoint $input.val()
        placemark = NewPlacemark center

        console.debug 'Init Yandex -> ', center
        console.debug 'Init PostGIS -> ', $input.val()

        map = new ymaps.Map "map",
            zoom: zoom
            center: center
        map.geoObjects.add placemark
        map.controls.add('mapTools').add 'zoomControl'

        map.events.add 'click', (e) ->
            if placemark
                map.geoObjects.remove placemark
                placemark.geometry.setCoordinates e.get('coordPosition')
            else
                placemark = NewPlacemark e.get('coordPosition')
            map.geoObjects.add placemark
            $input.val toPostgisPoint(placemark.geometry.getCoordinates())

            console.debug ''
            console.debug 'Set Yandex -> ', e.get('coordPosition')
            console.debug 'Set PostGIS -> ', $input.val()