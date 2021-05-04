#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library imports
import functools


def _wait_before_retry(func, sleep):
    if sleep:
        print(f"Retrying `{func.__name__}` in {sleep} seconds ...")
        time.sleep(sleep)


def retry(_func=None, max_tries=5, sleep=0):
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
                    pass

        return wrapper

    if _func is None:
        return decorator_retry
    else:
        return decorator_retry(_func)
