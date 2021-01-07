#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# In[8]:


def myreduce(num):
    ''' This functionm will return multiplication of n Natural numbers'''
    num_list=list(range(1,number+1))
    mul_of_elements=1
    
    for i in num_list:
        mul_of_elements*=i
        
    return num_list,mul_of_elements

#Input 
print("Input:")
number=int(input("Please insert the number :"))

#Function Execution

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Multiplication of List elements are :",output_value[1])


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[5]:


print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))


def myfilter(num_list):
    '''This function will filter even and odd numbers from list which are multiples of 5 '''
    num_even_list=[]
    num_odd_list=[]
    
    for i in num_list:
        if(i%5==0):
            if(i%2==0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)
                
    return num_even_list,num_odd_list


#Function Execution
output_value=myfilter(num_list)

#Output

print("Output:")
print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])


# Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[6]:


word="AcadGild"
#list Comprehension
output_list=[w.upper() for w in list(word)]
print("Output:")
print(output_list)

#Section 2
word_1=list('xyz')
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

#Section 3
word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

#Section 4
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

#Section 5
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

#Section 6
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)


# In[ ]:




