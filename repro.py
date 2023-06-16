"""
To the best of my (jfly's) knowledge, this roughly simulates a gunicorn
startup.
"""

# Step 1: set up configuration.
import logging.config
import gunicorn_conf
logging.config.dictConfig(gunicorn_conf.logconfig_dict)

# Step 2: monkey patch all the things!
from gevent import monkey
monkey.patch_all()

# Step 3: import the app and go to town.
import hello
hello.main()
