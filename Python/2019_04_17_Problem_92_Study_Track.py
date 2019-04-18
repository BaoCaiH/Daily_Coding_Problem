#!/usr/bin/env python
# coding: utf-8

# ### 2019 April 17th
#
# Problem: We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of `courseId` are `courseId`s. Return a sorted ordering of courses such that we can finish all courses.
#
# Return null if there is no such ordering.
#
# For example, given `{'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}`, should return `['CSC100', 'CSC200', 'CSCS300']`.

# In[15]:


def coursesTrack(courses, track = []):                              #
    if not track:                                                   # If we are looking for the first course
        for courseID, courseIDs in courses.items():                 # We search for a course
            if not courseIDs:                                       # That does not require anything
                otherCourses = coursesTrack(courses, [courseID])    # Recurse function on the remaining courses
                if otherCourses:                                    # If there is indeed a path
                    return otherCourses                             # Return it
        return None                                                 # Return None if there is nothing satisfy
                                                                    #
    if len(track) == len(courses):                                  # If we learned all the courses
        return track                                                # Dude, stop!
                                                                    #
    for courseID, courseIDs in courses.items():                     # If we are in the middle of the track
        if courseID not in track and        all(course in track for course in courseIDs):               # Search for a course we haven't learned
            otherCourses = coursesTrack(courses, track + [courseID])# and we satisfied all prerequisites
            if otherCourses:                                        # Check for a valid path
                return otherCourses                                 # and return
    return None                                                     # Else, return None


# In[25]:


courses1 = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
courses2 = {'CSC300': ['CSC100'], 'CSC200': ['CSC100'], 'CSC100': []}
courses3 = {'CSC300': ['CSC100'], 'CSC200': ['CSC100', 'CSC300'], 'CSC100': []}
courses4 = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100', 'CSC400'], 'CSC100': []}
courses5 = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100', 'CSC400'], 'CSC100': [], 'CSC400':[]}


# In[29]:


courses = [courses1, courses2, courses3, courses4, courses5]


# In[35]:


examples = 1
for course in courses:
    print('Example {}:'.format(examples))
    print('Given the courses and their respective prerequisites:')
    for ID, IDs in course.items():
        print(ID + ' : ' + str(IDs))
    print('The suggested path to study is {}'.format(coursesTrack(course)))
    print()
    examples += 1


# In[36]:


print('In example 2, the path suggested CSC300 before CSC200 simply because it was listed first.')
print()
print('In example 5, the path suggested CSC100 before CSC400 for the same reason')


# In[ ]:
