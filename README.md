This reproduces an infinite recursion issue that arises with a subtly
misconfigured gunicorn server (it imports a py file that imports `datadog`
which imports `ssl` and has who knows what other side effects).

    $ make repro
    python repro.py
    /home/jeremy/tmp/2023-06-dd-gevent-recursion-error/repro.py:13: MonkeyPatchWarning: Monkey-patching ssl after ssl has already been imported may lead to errors, including RecursionError on Python 3.6. It may also silently lead to incorrect behaviour on Python 3.7. Please monkey-patch earlier. See https://github.com/gevent/gevent/issues/1016. Modules that had direct imports (NOT patched): ['urllib3.util (/home/jeremy/tmp/2023-06-dd-gevent-recursion-error/.direnv/python-3.10/lib/python3.10/site-packages/urllib3/util/__init__.py)', 'urllib3.util.ssl_ (/home/jeremy/tmp/2023-06-dd-gevent-recursion-error/.direnv/python-3.10/lib/python3.10/site-packages/urllib3/util/ssl_.py)'].
      monkey.patch_all()
    About to create a urllib3 context
    Traceback (most recent call last):
      File "/home/jeremy/tmp/2023-06-dd-gevent-recursion-error/repro.py", line 17, in <module>
        hello.main()
      File "/home/jeremy/tmp/2023-06-dd-gevent-recursion-error/hello.py", line 14, in main
        context = create_urllib3_context()
      File "/home/jeremy/tmp/2023-06-dd-gevent-recursion-error/hello.py", line 10, in create_urllib3_context
        context.options |= options
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      File "/nix/store/6qk2ybm2yx2dxmx9h4dikr1shjhhbpfr-python3-3.10.11/lib/python3.10/ssl.py", line 620, in options
        super(SSLContext, SSLContext).options.__set__(self, value)
      [Previous line repeated 496 more times]
    RecursionError: maximum recursion depth exceeded while calling a Python object
    make: *** [Makefile:7: repro] Error 1
