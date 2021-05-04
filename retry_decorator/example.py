#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import retry_decorator


@retry_decorator.retry(max_tries=3, sleep=1)
def hw(name="World"):
    print(f"Hello {name}")
    raise ValueError


def main():
    hw()


if __name__ == "__main__":
    main()
