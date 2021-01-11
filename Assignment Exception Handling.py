#!/usr/bin/env python
# coding: utf-8

# 1.Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[3]:


def compute(number):
    try:
        result= number/0
        print(result)
    except:
        print("Number is not divisible by zero")
        
number= 5
compute(number)


# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# 
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# 
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[5]:


Subject= ["Americans","Indians"]
Verbs= ["play","watch"]
Objects= ["Baseball","Cricket"]

sentences= [(sub+ " "+ ver+ " "+ obj) for sub in Subject for ver in Verbs for obj in Objects]
for all_sentences in sentences:
    print(all_sentences)


# In[ ]:




