import os

# Step 1: effectively what happens when gunicorn starts up and configures
# logging (datadog imports urllib3).
import urllib3 as _

# Step 2: monkey patch all the things!
from gevent import monkey
monkey.patch_all()

# Step 3: try to create an ssl context with some custom options.
if os.environ["URLLIB3"] == "1":
    from urllib3.util.ssl_ import SSLContext
else:
    from ssl import SSLContext
print("About to create a SSLContext")
context = SSLContext()
context.options = 0
print(f"How about that context, eh? {context}")
