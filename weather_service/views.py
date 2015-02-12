from datetime import (
    datetime,
    timedelta,
    )

from pyramid.view import view_config

from forecast import Forecaster


@view_config(route_name='home', renderer='jsonp')
def forecast(request):
    raw_coords = request.params.get('coords')

    if raw_coords is None:
        request.response.status = 400
        return {'errors': 'No coordinates specified.'}

    coords = []
    raw_coords = raw_coords.split(",")
    for i in range(len(raw_coords)):
        if i % 2 == 0:
            coord = float(raw_coords[i]), float(raw_coords[i+1])
            coords.append(coord) 

    # For now assume a time interval of 1 hour, and start at now.
    interval = timedelta(hours=1)
    now = datetime.now()
    api_key = request.registry.settings.get('API_KEY')
    f = Forecaster(api_key)

    forecasts = []
    for i,c in enumerate(coords):
        time = now + (i*interval)
        forecast = f.forecast(*c, time=time)
        forecasts.append((c, forecast, time.strftime('%R')))
    request.response.status = 200
    return { 'forecasts': forecasts }
