from forecastio import load_forecast


DEFAULT_FIELDS = [
    'temperature',
    'humidity',
    'windSpeed',
    'windBearing',
    'precipProbability',
    'precipType',
    ]


class Forecaster:

    def __init__(self, key=None, fields=None):
        self.key = key
        if fields is None:
            self.fields = DEFAULT_FIELDS
        else:
            self.fields = fields

    def forecast(self, lat, lng, time):
        raw_data = load_forecast(
            self.key, lat, lng, time, units='us').currently()

        data = {}
        for f in self.fields:
            data[f] = getattr(raw_data, f, None) 

        return data
