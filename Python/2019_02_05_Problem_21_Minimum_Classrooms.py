#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 5th
# 
# Problem: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# 
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# In[66]:


def min_classrooms(lectures):
    lectures.sort()
    classrooms = []
    for start, end in lectures:
        if not classrooms:
            classrooms.append(end)
        else:
            for i, e in enumerate(classrooms):
                if start >= e:
                    classrooms[i] = end
                    break
            if end not in classrooms:
                classrooms.append(end)
    return len(classrooms)


# In[63]:


lect = [(30, 75), (0, 50), (60, 150), (75, 110), (100, 120)]


# In[67]:


print('Given the following lectures: {}'.format(lect))
print('The minimum required classrooms is {}'.format(min_classrooms(lect)))

