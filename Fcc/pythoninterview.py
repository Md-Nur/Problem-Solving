# -*- coding: utf-8 -*-
"""pythonInterview.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f-hKJHkzKG7Sa7a9jtu4q143j-hfgz0k

# WHY ANALYZE ALGORITHM ?
- Procedure or formula for solving a problem
- Some are so useful they have names:
    merge sort, bubble sort etc ...
- How can we compare the algos to know which is better ?

Imagine I came up with this function
"""

def sum1(n):
    '''
    Take a input of n and return the sum of 0 to n
    '''
    finalSum = 0
    for i in range(n+1):
        finalSum+=i
    return finalSum

sum1(5)

# And you give me this function
def sum2(n):
    '''
    Take a input of n and return the sum of 0 to n
    '''
    return (n*(n+1)/2)

sum2(5)

"""Funtion sum1 uses a for loop to  iteratively add across our range + 1 

Funtion sum2 makes use of a fromula to solve a problem
# OBJECTIVELY COMPARE THEM
- Memory to space
- time to run

Build in magic commands in note book

result in microseconds
"""

# Commented out IPython magic to ensure Python compatibility.
# %timeit sum1(100)

# Commented out IPython magic to ensure Python compatibility.
# %timeit sum2(100)

"""# Big O notation"""

def bigO(n):
    return 45*n**3+20*n**2+19
bigO(1)

bigO(2)

bigO(10)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from math import log
import matplotlib.pyplot as plt
# %matplotlib inline

# Setup runtime comparisons
n = np.linspace(1,10)
labels = ['Constant','Logarithmic','Linear','Log Linear','Quadratic','Cubic','Exponential']
bigO = [np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,2**n]

# Plot setup
plt.figure(figsize=(16,8))
plt.ylim(0,50)

for i in range(len(bigO)):
    plt.plot(n,bigO[i],label = labels[i])

plt.legend(loc=0)
plt.ylabel("Relative runtime")
plt.xlabel("n")

"""# BigO Examples 
## BigO 1 (Constant)
"""

def bigOConst(values):
    
    '''
    return the frist index value of the list values
    '''
    return values[0]

bigOConst([1,2,4,2,4,2,1,3,1])

"""## bigO 2 (Linear)"""

def bigOLin(values):
    '''
    return the all values of the list
    '''
    for i in values:
        print(i)

bigOLin([10,23,28,64,])

"""## Quadradic List"""

def bigOquad(lst):
    '''
    Prints pair of every item of the list
    '''
    for i in lst:
        for j in lst:
            print(i,j)
bigOquad([12,4,2,1,5,3,54])

def threeTime(n):
    for _ in range(3):
        for i in n:
            print(i)
threeTime("khela hobe")

def comp(lst):
    '''
    Fist element of the list
    First half element of the list
    First 10 element of the list (constant)
    '''
    print(lst[0])
    print(lst[:(len(lst)//2)])
    print('Number\n'*10)
lst = [1,3,9,25,2,4,2,6]
comp(lst)

def lstMatch(lst, match):
    return match in lst
lstMatch(lst,2)

lstMatch(lst,45)

def memory(n = 10):
    print("Memory!\n"*n)
memory(10)

import sys
n = 10
data = []
for _ in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length {0:3d} ; Size in bytes: {1:4d}'.format(a,b))
    data.append(n)

def anagram(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1)== sorted(s2) 

anagram("dog",'god')

anagram("clint east wood","old west action")

anagram("aa","bb")
