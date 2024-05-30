from contextlib import AbstractContextManager
from logging import getLogger
from time import perf_counter_ns
from typing import Callable

_timing_logger = getLogger(__file__)
_DEFAULT_LOG = _timing_logger.info


def set_log_func(func: Callable[[str], None]):
    """
    Set default log function for all follow-up contexts.
    :param func:
    :return:
    """
    global _DEFAULT_LOG
    _DEFAULT_LOG = func


class measure_time(AbstractContextManager):
    """
    Provides a simple context to keep track of time
    """

    def __init__(self, name: str = "", log_func: Callable[[str], None] = None):
        self.log_func = log_func if log_func else _DEFAULT_LOG
        self.name = name
        self.start = None
        self.value = None

    def __enter__(self):
        self.start = perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.value = (perf_counter_ns() - self.start) / 1e9
        self._print()

    def _print(self) -> None:
        """
        Print in seconds if above 1s, else in ms. Outputs to the log function.
        :return:
        """
        unit = "s"
        if self.value < 1:
            self.value *= 1000
            unit = "ms"
        if self.log_func:
            try:
                self.log_func(f"Context {self.name} took {self.value:.3f} {unit}")
            except:  # noqa: E722
                pass

    @property
    def elapsed(self) -> float:
        """
        Returns time elapsed since context entering in seconds.
        :return:
        """
        if self.value is None:
            return (perf_counter_ns() - self.start) / 1e9
        return self.value
