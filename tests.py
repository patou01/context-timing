import builtins
import logging
from time import sleep
from unittest import mock

from context_timing.context_timing import set_log_func, TimeThis


def test_print():
    logging.basicConfig(level=logging.INFO)

    with mock.patch.object(builtins, "print") as m:
        set_log_func(print)
        with TimeThis():
            sleep(0.1)
        m.assert_called_once()

    with mock.patch.object(logging, "info") as m:
        set_log_func(logging.info)
        with TimeThis():
            sleep(0.1)
        m.assert_called_once()

    logger = logging.getLogger()
    with mock.patch.object(logger, "info") as m:
        set_log_func(logger.info)
        with TimeThis():
            sleep(0.1)
        m.assert_called_once()

    def hello():
        pass

    set_log_func(hello)
    with TimeThis():
        sleep(0.1)
