#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 29th
# 
# Problem: The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# 
# Hint: The basic equation of a circle is x2 + y2 = r2.

# The [Monte Carklo](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/) method can be read from the hyperlink

# Basically, we generate a set of points, inside a 1x1 square, which has a area of 1 unit square and a circle, which r = 1/2. Therefore, it has the area of π/4 unit square. Then we can calculate π by calculating:
# 
# > 4 * Area_of_the_circle/Area_of_the_square
# 
# So:
# 
# > π = 4 * Number_of_points_in_the_circle/Number_of_points_in_the_square
# 
# Also to make it easier, the circle's center will be at the (0, 0) coordinate. With r = 1

# In[1]:


def R_Sq_Calculator(x, y):
    return x**2 + y**2


# In[2]:


import random


# In[8]:


circle_points = 0
square_points = 0
for _ in range(10000000):
    x = random.random()
    y = random.random()
    R_Sq = R_Sq_Calculator(x, y)
    if R_Sq <= 1:
        circle_points += 1
    square_points += 1
Pie = 4*circle_points/square_points
round(Pie, 3)

