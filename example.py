import logging
from time import sleep

from context_timing import TimeThis, set_log_func

logging.basicConfig(level=logging.INFO)

with TimeThis() as _:
    sleep(1)

set_log_func(print)
with TimeThis() as _:
    sleep(1)
