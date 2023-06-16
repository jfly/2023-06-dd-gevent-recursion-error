.bootstrapped: requirements.txt
	pip install -r requirements.txt
	touch .bootstrapped

.PHONY: repro
repro: .bootstrapped
	gunicorn
