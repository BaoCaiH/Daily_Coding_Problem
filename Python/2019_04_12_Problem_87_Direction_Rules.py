#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 12th
# 
# Problem: A rule looks like this:
# 
# `A NE B`
# 
# This means this means point A is located northeast of point B.
# 
# `A SW C`
# 
# means that point A is southwest of C.
# 
# Given a list of rules, check if the sum of the rules validate. For example:
# 
# `A N B
# B NE C
# C N A`
# 
# does not validate, since A cannot be both north and south of C.
# 
# `A NW B
# A N B`
# 
# is considered valid.

# In[143]:


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbour = {
            'N' : [],
            'S' : [],
            'E' : [],
            'W' : []
        }
        
def add_rule(nodeA, directions, nodeB):
    opposite = {
        'N' : 'S',
        'S' : 'N',
        'E' : 'W',
        'W' : 'E'
    }
    for direction in directions:
        if nodeA in nodeB.neighbour[opposite[direction]] or            nodeB in nodeA.neighbour[direction]:
            raise Exception
        else:
            nodeB.neighbour[direction].append(nodeA)
            nodeA.neighbour[opposite[direction]].append(nodeB)
            try:
                for node in nodeB.neighbour[opposite[direction]]:
                    add_rule(nodeA, direction, node)
            except Exception:
                nodeB.neighbour[direction].pop()
                nodeA.neighbour[opposite[direction]].pop()
                print('Invalid rules')


# In[144]:


a = Node('a')
b = Node('b')
c = Node('c')


# In[145]:


add_rule(a, 'N', b)
add_rule(b, 'NE', c)
add_rule(c, 'N', a)


# In[ ]:


a = Node('a')
b = Node('b')
c = Node('c')


# In[142]:


add_rule(a, 'NW', b)
add_rule(a, 'N', b)

