from datetime import datetime
import unittest

from pyramid import testing
from mock import patch

from views import forecast
from forecast import Forecaster


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_forecast_failure(self):
        request = testing.DummyRequest()
        resp = forecast(request)
        self.assertEqual('No coordinates specified.', resp['errors'])

    def test_coordinates(self):
        request = testing.DummyRequest()
        request.params = {'coords': '1,2'}
        with patch('forecast.Forecaster.forecast') as f_mock:
            fake_forecast = {
                'temperature': 1,
                'humidity': 2,
                'windSpeed': 3,
                'windBearing': 4,
                'precipProbability': 5,
                'precipType': 'rain',
                }
            f_mock.return_value = fake_forecast
            resp = forecast(request)
            # only one call for one set of coordinates
            self.assertEqual(f_mock.call_count, 1)
            # parses the args from query string
            self.assertEqual(f_mock.call_args[0], (1.0, 2.0))
            self.assertEqual(resp['forecasts'][0][1], fake_forecast)


class FakeForecastData:
    temperature = 1
    humidity = 2
    windSpeed = 3
    windBearing = 4
    precipProbability = 5
    precipType = 'rain'


class FakeForecast:
    def currently(self):
        return FakeForecastData()


class ForecastTests(unittest.TestCase):

    def test_forecast(self):
        f = Forecaster('FAKE_API_KEY')
        with patch('forecast.load_forecast') as f_mock:
            fake = FakeForecast()
            f_mock.return_value = fake
            now = datetime.now()
            data = f.forecast(1,2,now)
            self.assertEqual(data['temperature'], 1)
            self.assertEqual(data['humidity'], 2)
            self.assertEqual(data['windSpeed'], 3)
            self.assertEqual(data['windBearing'], 4)
            self.assertEqual(data['precipProbability'], 5)
            self.assertEqual(data['precipType'], 'rain')
