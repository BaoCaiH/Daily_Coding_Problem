#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 7th
# 
# Problem: Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# 
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

# In[104]:


class files:                                                    #
    def __init__(self, contents):                               # Create the file
        self.contents = contents                                # Put in the contents
        self.offset = 0                                         # Offseting is to move along the file without
        self.buffer = ''                                        # modifying. Buffer is to temporarily storing
                                                                #
    def read7(self):                                            # Read 7 characters
        start = self.offset                                     # Read from the old offset mark
        self.offset = min(self.offset + 7, len(self.contents))  # To the new offset mark, 7 steps away
        return self.contents[start : self.offset]               #
                                                                #
    def readN(self, n):                                         # Read N characters
        buffer = len(self.buffer)                               # Check the buffer
        if buffer > n:                                          # If the buffer is more than enough for this print
            buffer = self.buffer[:n]                            # Trim the buffer
            self.buffer = self.buffer[n:]                       # And return the sufficent amount of character
            return buffer                                       # If not
        if self.offset == len(self.contents):                   # Check the offset
            buffer = self.buffer                                # If it's already at the end of the file
            self.buffer = ''                                    # Clean the buffer
            return buffer                                       # And return it at the same time
        self.buffer = self.buffer + self.read7()                # Otherwise, increase the buffer with read7
        return self.readN(n)                                    # Then recurse


# In[124]:


file = input('Input anything: ')
a = files(file)
print('Starting with the file contains: {}'.format(a.contents))


# In[125]:


n = int(input('Enter an integer: '))
print('This will print the file, {} characters at a time, including spaces'.format(n))
b = '.'
while b:
    b = a.readN(n)
    print('"{}"'.format(b))

