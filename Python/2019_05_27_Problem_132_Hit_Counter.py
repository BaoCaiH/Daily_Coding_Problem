#!/usr/bin/env python
# coding: utf-8
"""2019 May 27th - Daily_Coding_Problem #132."""
# <markdown>
# ## 2019 May 27th - Daily_Coding_Problem #132
#
# Problem: Design and implement a HitCounter class that keeps track of
# requests (or hits). It should support the following operations:
#
# record(timestamp): records a hit that happened at timestamp
#
# total(): returns the total number of hits recorded
#
# range(lower, upper): returns the number of hits that
# occurred between timestamps lower and upper (inclusive)
#
# Follow-up: What if our system has limited memory?


# %%
memoryLimit = 128


class TimestampsFile:
    """A class for a records file."""

    def __init__(self):
        """Initialize the file."""
        self.timestamps = []


class HitCounter:
    """A class to record timestamps."""

    def __init__(self, memoryLimit=128):
        """Initialize the ledger."""
        self.currentRecords = TimestampsFile()
        self.usedUpFiles = []
        self.memoryLimit = memoryLimit

    def record(self, timestamp):
        """Record timestamp."""
        self.currentRecords.timestamps.append(timestamp)
        if len(self.currentRecords.timestamps) == self.memoryLimit:
            self.usedUpFiles.append(self.currentRecords)
            self.currentRecords = TimestampsFile()

    def total(self):
        """Return the total number of records."""
        return (self.memoryLimit*len(self.usedUpFiles)) + \
            len(self.currentRecords.timestamps)

    def range(self, lower, upper):
        """Return the number of timestamps between a period."""
        if lower < self.usedUpFiles[0].timestamps[0] or\
           upper > self.currentRecords.timestamps[-1]:
            print('The boundaries are out of range')
            return None
        startIndex = None
        counter = None
        endIndex = None
        for file in self.usedUpFiles:
            if not startIndex:
                if file.timestamps[0] <= lower <= file.timestamps[-1]:
                    startIndex = file.timestamps.index(lower)
                    counter = len(file.timestamps[startIndex:])
            else:
                if file.timestamps[0] <= upper <= file.timestamps[-1]:
                    endIndex = file.timestamps.index(upper)
                    counter += len(file.timestamps[:endIndex+1])
                    break
                else:
                    counter += self.memoryLimit
        if not startIndex:
            startIndex = self.currentRecords.timestamps.index(lower)
            endIndex = self.currentRecords.timestamps.index(upper)
            counter = endIndex + startIndex + 1
        if not endIndex:
            endIndex = self.currentRecords.timestamps.index(upper)
            counter += len(self.currentRecords.timestamps[:endIndex+1])
        return counter


# %%
records = HitCounter()
for i in range(11234):
    records.record(i)
# %%
records.range(456, 1325)
