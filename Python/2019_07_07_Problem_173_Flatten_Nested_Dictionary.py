#!/usr/bin/env python
# coding: utf-8
"""2019 July 7th - Daily_Coding_Problem #173."""
# <markdown>
# ## 2019 July 7th - Daily_Coding_Problem #173
#
# This problem was asked by Stripe.
#
# Write a function to flatten a nested dictionary.
# Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# `{
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }`
#
# it should become:
#
# `{
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }`
#
# You can assume keys do not contain dots in them,
# i.e. no clobbering will occur.


# %%
def flatten(nestedDict):
    """Flatten a nested dictionary."""
    if not isinstance(nestedDict, dict):
        return nestedDict
    unnest = {}
    for key, value in nestedDict.items():
        unnestVals = flatten(value)
        if isinstance(unnestVals, dict):
            for k, v in unnestVals.items():
                unnest[key + '.' + k] = v
        else:
            unnest[key] = unnestVals
    return unnest


# %%
example = {'key': 3,
           'foo': {'a': 5,
                   'bar': {'baz': 8}}}
# %%
flatten(example)
