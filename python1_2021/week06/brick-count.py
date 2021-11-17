#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 



make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''


# In[ ]:


def make_bricks(number_small, number_large, goal):
    
    small_size = 1
    large_size = 5
    large_bricks_used = 0
    small_bricks_used = 0
    space_used = 0
    print(space_used)
    
    print(number_large)
    print(large_bricks_used)
    print("Goal: ", goal)
    
    while large_bricks_used <= number_large:
        while space_used <= goal:
            print("large bricks used: ", large_bricks_used)
            print("Space left: ", space_used)
            large_bricks_used += 1
            space_used += large_size
            
    while small_bricks_used <= number_small:
        while space_used <= goal:
            print("small bricks used: ", small_bricks_used)
            print("Space left: ", space_used)
            small_bricks_used += 1
            space_used += small_size        


# In[ ]:


make_bricks(3,1,8)


# In[ ]:


make_bricks(3,1,9)


# In[ ]:


make_bricks(3,2,10)


# In[ ]:


make_bricks(3,2,10)


# In[ ]:





# In[ ]:




