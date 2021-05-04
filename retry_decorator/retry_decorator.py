#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library imports
import functools
import time
import traceback
import warnings


def _wait_before_retry(func, sleep):
    if sleep:
        print(f"Retrying `{func.__name__}` in {sleep} seconds ...")
        time.sleep(sleep)


def _decorator_retry_warning(func, try_i):
    warning_msg = [
        f"ERROR WARNING: function call `{func.__name__}` failed on try #{try_i}",
        "Traceback:",
        traceback.format_exc(),
    ]
    warning_msg = "\n" + "\n".join(warning_msg)
    warnings.warn(warning_msg)


def retry(_func=None, max_tries=5, sleep=0):
    """A decorator to retry the function if it fails."""

    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            ret = None
            for try_i in range(1, max_tries + 1):

                try:
                    ret = func(*args, **kwargs)
                    if ret is not None:
                        # Escape the loop if `func` returns a value.
                        return ret
                    else:
                        # Escape the loop if `func` runs without an error,
                        # but returns no value.
                        break

                except Exception as e:
                    # Show warning when `func` raises an error
                    _decorator_retry_warning(func, try_i)

                _wait_before_retry(func, sleep)

        return wrapper

    if _func is None:
        return decorator_retry
    else:
        return decorator_retry(_func)
