# A simple pyramid service to fetch weather information from forecast.io

flightplan-service is a simple webservice that generates forecast information
for several points along a flightplan (or other geographical route).

## Endpoints

`/` is the only endpoint, and only allows `GET` requests. The only allowed
arguments are `coords`, a flattened string of lat and lng coordinates, and
`interval`, a decimal representation of hours between forecasts for each point.

## Example

A `GET` on `http://example.com/?coords=0,0,1,1&interval=0.5` would return
forecast data for the coordinate 0,0, and for 1,1, with the data for 0,0
corresponding to the weather now and the weather at 1,1 corresponding to the
weather in 30 minutes.

## Installation

For either the development or production install, you must get an API key from
developer.forecast.io

### Development
Run `make dev_setup`. Edit weather_service.ini to add your api key in the
provided value.

Run `make run`.

### Production
Run `make prod_setup`. Edit weather_service.ini to add your api key in the
provided value.

Run `make start_serve`. To stop the daemonized webservice run `make stop_serve`.
