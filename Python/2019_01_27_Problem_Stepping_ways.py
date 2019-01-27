#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ## 2019 January 27th
# 
# Problem: There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# 
# For example, if N is 4, then there are 5 unique ways:
# 
# 1, 1, 1, 1
# 
# 2, 1, 1
# 
# 1, 2, 1
# 
# 1, 1, 2
# 
# 2, 2
# 
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# In[11]:


def ways_to_step(N, step_set):
    counter = 0
    for step in step_set:                               # This is how we implement a step set
        if N - step < 0:                                # So I also decide to not over step the stairs
            break
        elif 0 <= N - step <= min(step_set):            # If after this step, there is no more step to step
            counter += 1                                # This is one way to step            
        else:                                           # Otherwise
            counter += ways_to_step(N - step, step_set) # We LOOP, by calling the function inside it
    return counter


# In[13]:


print('Given the stairs of {} steps and two ways to step 1 or 2. There are {} ways to step'.format(4,
                                                                                                  ways_to_step(4, [1, 2])))


# In[18]:


steps = int(input('Give the number of steps: '))
step_set = input('Give the set of step you can step in the form of numbers separated by commas (i.e. 1,2,3): ')
step_set = [int(step) for step in step_set.split(',')]
print(step_set)
ways_to_step(steps, step_set)

