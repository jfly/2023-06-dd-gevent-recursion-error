import logging

# Unused, but this causes trouble because this file gets imported before
# gunicorn does gevent monkeypatching, and `datadog` goes on to import an
# unpatched `ssl`.
import datadog as _

class Formatter(logging.Formatter):
    pass
