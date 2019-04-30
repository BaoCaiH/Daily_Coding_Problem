#!/usr/bin/env python
# coding: utf-8
"""2019 April 30th - Daily_Coding_Problem #105."""
# <markdown>
# ## 2019 April 30th - Daily_Coding_Problem #105
#
# Problem: Given a function f, and N return a debounced f of N milliseconds.
#
# That is, as long as the debounced f continues to be invoked,
# f itself will not be called for N milliseconds.
#
# Comment: This problem is way over my head, so I learned something new today
#
# Source:
# https://jonlabelle.com/snippets/view/python/python-debounce-decorator-function
import time


# %%
def debounce(wait):
    """Postpone a functions execution until after some time has elapsed.

    :type wait: int
    :param wait: The amount of Seconds to wait before execution.
    """
    from threading import Timer

    # The function will be passed here
    def decorator(fun):
        # The variables will be passed here
        def debounced(*args, **kwargs):
            # If try printing args and kwargs here we can see all the variables
            # print(args)
            # print(kwargs)
            def call_it():
                # Based on LEGB rules, the function can now call variables
                # from the previous layer
                fun(*args, **kwargs)
            # If the timer has started, interrupt it
            try:
                debounced.t.cancel()
            except AttributeError:
                pass
            # Assign and restart timer
            debounced.t = Timer(wait, call_it)
            debounced.t.start()
        return debounced

    return decorator


# %%
# Set debounce time here
@debounce(1)
def printAllThese(a, b, c):
    """Test function."""
    print(a)
    print(b)
    print(c)


# %%
# It will not print the first 2 lines since the sleep time is less than the
# debounce time set above on line 49
# It will not work correctly 100% of the time with sleep time of 1 because
# the actual sleep time is dependent on the processing power as well
printAllThese(3, 6, 1)
time.sleep(0.9)
printAllThese(6, 9, 1)
printAllThese(10, 10, 10)
time.sleep(1.1)
printAllThese(324, 234, 64)
printAllThese(1234, 3, 65)
