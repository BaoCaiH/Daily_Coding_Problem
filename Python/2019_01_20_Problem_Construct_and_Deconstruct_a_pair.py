#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 20th
# 
# Problem: cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# 
# Given this implementation of cons:
# 
# `def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair`
#     
# Implement car and cdr.

# In[34]:


def cons(a, b):        # The trick of this question is in the strange structure of this function `cons`
    def pair(f):       # It defines another function inside, but that's not the strange thing
        return f(a, b) # The secondary function ends here
    return pair        # Then the main function ends too


# In[39]:


print('A pair of {} and {} will be created'.format(6, 7))
p = cons(6, 7)         # Guess what type this guys is


# In[35]:


print('The type of the pair is a {}, strange right?'.format(type(p)))


# In[36]:


# Basically, the pair is now a function, which stores 2 digits 6 and 7 in this case
# What's left in the pair now is the function pair(f)
# So the pair will substitute any function `f`, wrap around 6 and 7
# So pair(something) -> something(a, b) and we need `something` to release only a or b


# In[37]:


# This is more than enough
def return_a(a, b):
    return a
def return_b(a, b):
    return b


# Everything in one function for anyone who feels like it
# 
# `def car(pair):
#     def return_a(a, b):
#         return a
#     return pair(return_a)`
# 
# `def cdr(pair):
#     def return_b(a, b):
#         return b
#     return pair(return_b)`

# In[42]:


# p(return_a)

# p(return_b)


# In[47]:


# But the problem asked for a function to wrap around the pair like `car(pair)`
# Let's do just that
# So tedious
def car(pair):
    return pair(return_a)
def cdr(pair):
    return pair(return_b)


# In[49]:


# car(p)

# cdr(p)


# In[54]:


print('car(cons(6, 7)) returns {}'.format(car(cons(6, 7))))


# In[53]:


print('cdr(cons(6, 7)) returns {}'.format(cdr(cons(6, 7))))

