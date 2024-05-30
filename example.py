from time import sleep

from context_timing import measure_time, set_log_func

set_log_func(print)
with measure_time():
    sleep(0.1)
