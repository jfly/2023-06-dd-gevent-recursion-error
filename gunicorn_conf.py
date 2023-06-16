wsgi_app = "hello:app"

bind = '0.0.0.0:5000'
worker_class = 'gevent'
workers = 1

# Capture error logs to `stdout` (access logs are disabled by default)
logconfig_dict = {
    'version': 1,
    'formatters': {
        'json': {
            'class': 'log_formatter.Formatter',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'json',
        },
    },
    'disable_existing_loggers': False,
    'loggers': {
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
}
