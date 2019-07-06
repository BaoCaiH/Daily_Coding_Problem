#!/usr/bin/env python
# coding: utf-8
"""2019 July 5th - Daily_Coding_Problem #171."""
# <markdown>
# ## 2019 July 5th - Daily_Coding_Problem #171
#
# This problem was asked by Amazon.
#
# You are given a list of data entries that represent entries and
# exits of groups of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time.
#
# Find the busiest period in the building, that is, the time with the most
# people in the building. Return it as a pair of (start, end) timestamps.
# You can assume the building always starts off and ends up empty,
# i.e. with 0 people inside.


# %%
def busiestTime(entries):
    """Return the busiest period of time."""
    start = None
    populationRecord = {}
    population = 0
    for entry in entries:
        if not start:
            start = entry['timestamp']
        else:
            if population not in populationRecord:
                populationRecord[population] = []
            populationRecord[population].append((start, entry['timestamp']))
            start = entry['timestamp']
        if entry['type'] == 'enter':
            population += entry['count']
        else:
            population -= entry['count']
    return populationRecord[max(populationRecord.keys())][0]


# %%
entries = []
entries.append({"timestamp": 1526579928, 'count': 3, "type": "enter"})
entries.append({"timestamp": 1526580382, 'count': 2, "type": "exit"})
entries.append({"timestamp": 1526580383, 'count': 10, "type": "enter"})
entries.append({"timestamp": 1526580384, 'count': 5, "type": "exit"})
entries.append({"timestamp": 1526580390, 'count': 5, "type": "enter"})
entries.append({"timestamp": 1526580393, 'count': 10, "type": "exit"})
# %%
busiestTime(entries)
