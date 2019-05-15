#!/usr/bin/env python
# coding: utf-8
"""2019 May 15th - Daily_Coding_Problem #120."""
# <markdown>
# ## 2019 May 15th - Daily_Coding_Problem #120
#
# Problem: Implement the singleton pattern with a twist.
# First, instead of storing one instance, store two instances.
# And in every even call of getInstance(),
# return the first instance and in every odd call of getInstance(),
# return the second instance.
#
# Note to self: I don't fully understand my solution though
#
# I think I assign the values or instances to the class variable __instances
# so it is marked, like, permanently even when the whole class is called again
#
# After that, just switch between values. Maybe, explain to me in the future,
# thanks, self


# %%
class twistedSingleton:
    """A singleton pattern with a twist."""

    __instance = None
    evenCalls = False

    @staticmethod
    def getInstance():
        """Define a static access method."""
        if not twistedSingleton.__instance:
            twistedSingleton()
        twistedSingleton.evenCalls = not twistedSingleton.evenCalls
        return twistedSingleton.__instance[int(not twistedSingleton.evenCalls)]

    def __init__(self, value=None):
        """Define a virtually private constructor."""
        if twistedSingleton.__instance:
            raise Exception('This class is a singleton!')
        else:
            if not value:
                value = self
            twistedSingleton.__instance = ['first '+str(value),
                                           'second '+str(value)]


# %%
huhu = twistedSingleton()

# %%
huhu.getInstance()
