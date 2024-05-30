# context-timing

A python context manager for timing of a block. Somewhat similar to [contexttimer](https://github.com/brouberol/contexttimer) or
[timethis](https://github.com/meribold/timethis).

Uses `perf_counter()` underneath. The use case does not warrant looking at `perf_counter_ns()`.

# Use case

## Main use case

This package is **not** intended to measure perfomance like timeit would do. The main use case here is to get a quick way to
display how long a block of code takes to execute. For instance if you have a large amount of code that runs, and have a
feeling that the duration of some functions could help you understand the behaviour. This package lets you easily
add a display of this timing.

## In-between timing

The package, similarly to `contexttimer` lets you get the time since start.

```python
from context_timing import measure_time

with measure_time() as m:
    sleep(1)
    value = abs(m.elapsed - 1)  # True

```

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
