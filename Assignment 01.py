#!/usr/bin/env python
# coding: utf-8

# Question 01:  1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.
#     

# In[2]:


n=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        n.append(str(i))
print(','.join(n))


# Question 02: Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
# 

# In[12]:


first_name= input()
last_name= input()
print(last_name, " ",first_name)


# Write a Python program to find the volume of a sphere with diameter 12 cm 
# Formula: V=4/3 * π * r 3

# In[15]:


diameter= 12
r= diameter/2
pi= 3.141
v= 4/3 * pi * r**3
print("Volumne of a sphere: ", v)


# In[ ]:




