sys-deps:
	sudo apt-get install python-virtualenv

bin/python:
	virtualenv .

bin/pip:
	virtualenv .

venv: bin/python
	

clean:
	- rm -rf bin/ include/ lib/ local/
