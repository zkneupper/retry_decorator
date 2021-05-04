#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library imports
import functools


def retry(_func=None, max_tries=5, sleep=0):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = None
            try:
                ret = func(*args, **kwargs)
                if ret is not None:
                    return ret
                else:
                    break
            except Exception as e:
                pass

        return wrapper

    if _func is None:
        return decorator_retry
    else:
        return decorator_retry(_func)
