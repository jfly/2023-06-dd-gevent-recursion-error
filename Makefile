.bootstrapped: requirements.txt
	pip install -r requirements.txt
	touch .bootstrapped

.PHONY: repro
repro: .bootstrapped
	URLLIB3=1 python repro.py
