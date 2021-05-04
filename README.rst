=========
Retry Decorator
=========

A decorator to retry the function if it fails.


Example
--------

Using the `@retry_decorator.retry` decorator:

.. code-block:: python

    import retry_decorator

    @retry_decorator.retry(max_tries=3, sleep=1)
    def hw(name="World"):
        print(f"Hello {name}")
        raise ValueError

    hw()

    >>> Hello World
    >>> /Users/retry_decorator/retry_decorator/retry_decorator.py:25: UserWarning:
    >>> ERROR WARNING: function call `hw` failed on try #1
    >>> Traceback:
    >>> Traceback (most recent call last):
    >>>   File "/Users/retry_decorator/retry_decorator/retry_decorator.py", line 39, in wrapper
    >>>     ret = func(*args, **kwargs)
    >>>   File "/Users/retry_decorator/retry_decorator/example.py", line 11, in hw
    >>>     raise ValueError
    >>> ValueError
    >>>
    >>>   warnings.warn(warning_msg)
    >>> Retrying `hw` in 1 seconds ...
    >>> Hello World
    >>> /Users/retry_decorator/retry_decorator/retry_decorator.py:25: UserWarning:
    >>> ERROR WARNING: function call `hw` failed on try #2
    >>> Traceback:
    >>> Traceback (most recent call last):
    >>>   File "/Users/retry_decorator/retry_decorator/retry_decorator.py", line 39, in wrapper
    >>>     ret = func(*args, **kwargs)
    >>>   File "/Users/retry_decorator/retry_decorator/example.py", line 11, in hw
    >>>     raise ValueError
    >>> ValueError
    >>>
    >>>   warnings.warn(warning_msg)
    >>> Retrying `hw` in 1 seconds ...
    >>> Hello World
    >>> /Users/retry_decorator/retry_decorator/retry_decorator.py:25: UserWarning:
    >>> ERROR WARNING: function call `hw` failed on try #3
    >>> Traceback:
    >>> Traceback (most recent call last):
    >>>   File "/Users/retry_decorator/retry_decorator/retry_decorator.py", line 39, in wrapper
    >>>     ret = func(*args, **kwargs)
    >>>   File "/Users/retry_decorator/retry_decorator/example.py", line 11, in hw
    >>>     raise ValueError
    >>> ValueError
    >>>
    >>>   warnings.warn(warning_msg)
