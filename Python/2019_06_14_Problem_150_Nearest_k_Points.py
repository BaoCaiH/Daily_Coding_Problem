#!/usr/bin/env python
# coding: utf-8
"""2019 June 14th - Daily_Coding_Problem #150."""
# <markdown>
# ## 2019 June 14th - Daily_Coding_Problem #150
#
# This problem was asked by LinkedIn.
#
# Given a list of points, a central point, and an integer k,
# find the nearest k points from the central point.
#
# For example, given the list of points [(0, 0), (5, 4), (3, 1)],
# the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].


# %%
def nearestKPoints(points, centre, k):
    """Find k nearest points from the centre."""
    distancePoints = {}
    for point in points:
        distance = ((point[0]-centre[0])**2 + (point[1]-centre[1])**2)**0.5
        distance = round(distance, 2)
        if distance not in distancePoints:
            distancePoints[distance] = []
        distancePoints[distance].append(point)
    distances = sorted(list(distancePoints.keys()))
    sortedPoints = []
    for distance in distances:
        sortedPoints = sortedPoints + distancePoints[distance]
    return sortedPoints[:k]


# %%
a = {1: 34, 12: 234, 8: 24}
b = sorted(list(a.keys()))
b
# %%
points = [(0, 0), (5, 4), (3, 1)]
centre = (1, 2)
k = 2
nearestKPoints(points, centre, k)
