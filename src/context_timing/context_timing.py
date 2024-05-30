
from logging import getLogger, Logger, getLevelName
from contextlib import AbstractContextManager
from time import perf_counter
from typing import Callable

_timing_logger = getLogger(__file__)
_DEFAULT_LOG = _timing_logger.info


def set_log_func(func: Callable[[str], None]):
    global _DEFAULT_LOG
    _DEFAULT_LOG = func


class measure_time(AbstractContextManager):
    def __init__(self, name: str = "", log_func: Callable[[str], None] = None):
        self.log_func = log_func if log_func else _DEFAULT_LOG
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        value = perf_counter() - self.start
        unit = "s"
        if value < 1:
            value *= 1000
            unit = "ms"

        if self.log_func:
            try:
                self.log_func(f"Context {self.name} took {value} {unit}")
            except:
                pass