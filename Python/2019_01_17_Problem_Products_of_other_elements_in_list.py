#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 17th
# 
# Problem: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# In[46]:


def product_of_other_elements(array):
    """
    return a new array such that
    each element at index i of the new array is the product
    of all the numbers in the original array except the one at i
    """
    
    # This problems need numpy
    import numpy as np
    
    print('The original array/list was ', end = '')
    print(array)
    
    # Function start here
    
    return_array = []
    
    for i in range(len(array)):
        copy_array = array.copy()
        copy_array[i] = 1
        product = np.prod(copy_array)
        return_array.append(product)
    
    print('The output is ', end = '')
    print(return_array)
    
    return return_array
        


# In[49]:


input_array = [3, 2, 1, 4, 7, 2, 8, 3]
output_array = product_of_other_elements(input_array)

