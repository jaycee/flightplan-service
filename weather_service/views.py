from pyramid.view import view_config

@view_config(route_name='home', renderer='json')
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

    return {'coordinates': coords}
