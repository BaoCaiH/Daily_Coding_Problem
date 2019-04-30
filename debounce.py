#!/usr/bin/env python
# coding: utf-8
"""A debounce function on python."""
# <markdown>
# For future use of course


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
