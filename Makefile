APP=lib/python2.7/site-packages/weather-service.egg-link

sys-deps:
	sudo apt-get install python-virtualenv

bin/python:
	virtualenv .

bin/pip:
	virtualenv .

bin/pserve: bin/pip
	bin/pip install -r requirements.txt

bin/py.test: bin/pip
	bin/pip install -r requirements.txt

bin/gunicorn:
	bin/pip install -r requirements.txt

$(APP): bin/python
	bin/python setup.py develop

run: $(APP) bin/pserve 
	bin/pserve --reload development.ini

test: bin/py.test
	bin/py.test -s weather_service/tests.py

clean:
	- rm -rf bin/ include/ lib/ local/
	- rm -rf weather_service.egg-info

start_serve: $(APP) bin/gunicorn
	bin/gunicorn -w 4 -p weatherservice.pid -D weather_service:main

stop_serve:
	- kill -s 3 `cat weatherservice.pid`
