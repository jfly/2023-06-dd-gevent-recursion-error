This reproduces an infinite recursion issue that arises with a subtly
misconfigured gunicorn server (it imports a py file that imports `datadog`
which imports `ssl` and has who knows what other side effects).

    $ make repro
    Starting gunicorn 20.1.0
    Listening at: http://0.0.0.0:5000 (216900)
    Using worker: gevent
    Booting worker with pid: 216901
    /home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/workers/ggevent.py:38: MonkeyPatchWarning: Monkey-patching ssl after ssl has already been imported may lead to errors, including RecursionError on Python 3.6. It may also silently lead to incorrect behaviour on Python 3.7. Please monkey-patch earlier. See https://github.com/gevent/gevent/issues/1016. Modules that had direct imports (NOT patched): ['urllib3.util.ssl_ (/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/urllib3/util/ssl_.py)', 'urllib3.util (/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/urllib3/util/__init__.py)'].
      monkey.patch_all()
    Exception in worker process
    Traceback (most recent call last):
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/arbiter.py", line 589, in spawn_worker
        worker.init_process()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/workers/ggevent.py", line 146, in init_process
        super().init_process()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
        self.load_wsgi()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
        self.wsgi = self.app.wsgi()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
        self.callable = self.load()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
        return self.load_wsgiapp()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
        return util.import_app(self.app_uri)
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/.direnv/python-3.10/lib/python3.10/site-packages/gunicorn/util.py", line 359, in import_app
        mod = importlib.import_module(module)
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/importlib/__init__.py", line 126, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
      File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
      File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
      File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
      File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
      File "<frozen importlib._bootstrap_external>", line 883, in exec_module
      File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/hello.py", line 14, in <module>
        context = create_urllib3_context()
      File "/home/jeremy/tmp/2023-06-15-pyhack-2/hello.py", line 12, in create_urllib3_context
        context.options |= options
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      [Previous line repeated 485 more times]
    RecursionError: maximum recursion depth exceeded while calling a Python object
    Worker exiting (pid: 216901)
    Shutting down: Master
    Reason: Worker failed to boot.
