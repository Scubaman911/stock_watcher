"""
Data utilities for the stock data models.
"""
import os
import time
import functools
import logging

def percentage_change(current_value: float, previous_value: float):
    x = (current_value - previous_value) / previous_value
    x_as_pcnt = x * 100
    return x_as_pcnt


def call_on_schedule(func: callable):
    secs = int(os.getenv("SCHEDULE_SECONDS", 60))
    minutes = int(os.getenv("SCHEDULE_MINUTES", 0))

    timer_secs = secs + (minutes * 60)
    timer = timer_secs

    while timer:        
        time.sleep(1)
        timer -= 1
        if timer == 0:
            logging.info(f"{func.__name__} is being called...")
            start = time.perf_counter()
            func()
            logging.info(f"{func.__name__} has finished, resetting timer...")
            stop = time.perf_counter()
            logging.info(f"Processing took {stop - start:2f} seconds to complete.")
            timer = timer_secs
      
def on_schedule(func):
    @functools.wraps(func)
    def wrapper():
        logging.info(f"{func.__name__} has been submitted to be called on a schedule.")
        call_on_schedule(func)
    return wrapper