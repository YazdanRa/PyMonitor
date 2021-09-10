import functools
import resource
from matplotlib import pyplot as pd
from threading import Thread
from datetime import datetime
from time import sleep

from .templates import time_result


def monitor(measure):
    def time_monitor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            func(*args, **kwargs)
            end_time = datetime.now()

            print(time_result.format(
                start_time=start_time.time(),
                end_time=end_time.time(),
                process_time=end_time - start_time,
            ))

        return wrapper

    def cpu_monitor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            thread = Thread(target=func)
            thread.start()

            # TODO: override if provided
            refresh_period = 0.1  # Seconds

            cpu_usage = dict()
            while thread.is_alive():
                sleep(refresh_period)
                cpu_usage[datetime.now()] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

            print("======================================")
            for time, usage in cpu_usage.items():
                print(time.time(), ":  ", usage)

            pd.plot(range(len(cpu_usage)), cpu_usage.values())

            try:
                pd.savefig("figures/figure.png")
            except FileNotFoundError:
                import os
                os.mkdir("figures")
                pd.savefig("figures/figure.png")

        return wrapper

    monitor_map = dict(
        time=time_monitor,
        cpu=cpu_monitor,
    )

    if measure not in monitor_map.keys():
        raise AssertionError(
            f"'{measure}' is not a valid measure! "
            f"Please choose a correct measure: {list(monitor_map.keys())}"
        )

    return monitor_map[measure]
