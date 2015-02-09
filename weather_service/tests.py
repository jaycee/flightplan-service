import unittest

from pyramid import testing

from .views import forecast


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_coordinates(self):
        request = testing.DummyRequest()
        request.params = {'coords': '1,2'}
        parsed_coords = forecast(request).get('coordinates')
        self.assertEqual(parsed_coords, [(1.0, 2.0)])
