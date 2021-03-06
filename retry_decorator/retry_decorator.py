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


def _infinite_loop_warning(max_tries):
    if max_tries is None:
        warnings.warn("INFINITE LOOP possible because max_tries is None!")


def _decorator_retry_warning(func, try_i):
    warning_msg = [
        f"ERROR WARNING: function call `{func.__name__}` failed on try #{try_i}",
        "Traceback:",
        traceback.format_exc(),
    ]
    warning_msg = "\n" + "\n".join(warning_msg)
    warnings.warn(warning_msg)


def retry(
    _func=None,
    max_tries=5,
    sleep=0,
    raise_final_try_error=True,
    suppress_warnings=False,
):
    """A decorator to retry the function if it fails.

    max_tries: An integer for the number of tries, or None.
        max_tries=None could cause an infinite loop

    sleep: A float or integer for the number of seconds to
        wait between tries.

    suppress_warnings: A boolean for whether or not to suppress
        warnings raised when the decorated function fails in a try

    """

    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            ret = None

            _infinite_loop_warning(max_tries)

            try_i = 1

            while True:

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
                    if not suppress_warnings:
                        _decorator_retry_warning(func, try_i)

                    if max_tries is not None:
                        if try_i >= (max_tries):
                            if raise_final_try_error:
                                raise e
                            else:
                                break

                try_i += 1

                _wait_before_retry(func, sleep)

        return wrapper

    if _func is None:
        return decorator_retry
    else:
        return decorator_retry(_func)
