#!/usr/bin/python3
from weakref import finalize


def raise_exception():
    try:
        raise KeyboardInterrupt
    finally:
        print('Exception raised')
