#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[3]:


class Triangle():
    def __init__(self,a,b,c):
        self.a= float(a)
        self.b= float(b)
        self.c= float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))
class Area_of_triangle(Triangle):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    
    def area(self):
        s= (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5
t= Area_of_triangle(a,b,c)
print("Area: {}".format(t.area()))
    


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# In[10]:



def filter_long_words(words, n):
    list_of_words = []
    for i in range(len(words)):
        if len(words[i])> n:
            list_of_words.append(words[i])
    return list_of_words
inputlist= ["shailja","sengar","i","am"]
n=3
print(str(filter_long_words(inputlist, n)))


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[5]:


def length_of_string(words):
    return list(map(lambda x: len(x), words))
words= ["sh","ai","shailja"]
print(str(length_of_string(words)))


# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[11]:


def character_checker(char):
    if char=="a" or char=="A" or char=="e" or char=="E" or char=="i" or char=="I" or char=="o" or char=="O" or char=="u" or char=="U":
        return True
    else:
        return False
char= input()
character_checker(char)


# In[ ]:





# In[ ]:





# In[ ]:




