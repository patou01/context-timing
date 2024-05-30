# context-timing

A python context manager for timing of a block. Similar to contexttimer or 
[timethis](https://github.com/meribold/timethis).

# How to use

## Basic

```python
from context_timing import measure_time

with measure_time():
    sleep(1)

```

## Set output steam for multiple calls

```python
from context_timing import measure_time, set_log_func

set_log_func(print)

with measure_time():
    sleep(1)

with measure_time():
    sleep(2)
```

## Redirect the output for one measurement

```python
import logging
from context_timing import measure_time, set_log_func

set_log_func(print)

with measure_time(logging.info):
    sleep(1)

with measure_time():
    sleep(2)
```