#!/usr/bin/env python
# coding: utf-8

# Q1.Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number

# In[1]:


a=[]
total_no=int(input("total no to be accepted"))
for i in range((total_no)):
    b=int(input("accept number"))
    if(b%2)==0:
        a.append(b)
print("even number from 1 to 10 is",a)
        


# Q2.CREATE NOTEBOOK ON LIST COMPREHENSION

# 1.Iterating through a string Using List Comprehension

# In[2]:


game=[player for player in "cricket"]
print(game)


# 2.Conditionals in List Comprehension

# In[4]:


scorecard=[x for x in range(11)  if x%2!=0]
print("scorecard of odd number is",scorecard)


# 3.Nested IF with List Comprehension

# In[6]:


scorecard=[x for x in range(11)  if x%2!=0 if x%3==0] 
print(scorecard)


# 4.if...else With List Comprehension

# In[8]:


scorecard=['won' if x%2==0 else 'loss' for x in range(11)] 
print(scorecard)
print("\nwhen surya yadav come in even postion batting order winning count out of 10 is:- ")
scorecard.count('won')


# Q3.DICTIONARY CREATION PROGRAM 

# In[15]:



n=int(input("Input a number "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x

print(d) 


# Q4.There is a robot which wants to go the charging point to charge itself.
# The robot moves in a 2-D plane from the original point (0,0). The robot can
# move toward UP, DOWN, LEFT and RIGHT with given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
# The numbers after the direction are steps.
# Write a program to compute the distance between the current position after
# a sequence of movement and original point. If the distance is a float, then
# just print the nearest integer (use round() function for that and then convert
# it into an integer).
# Input Format:
# The first line of the input contains a number n which implies the number of
# directions to be given.
# The next n lines contain the direction and the step separated by a space.
# Output Format:
# Print the distance from the original position to the current position.
# 

# In[33]:


import math
#Init vars
pos=[0,0]
moves={"UP":[0,1],
       "DOWN":[0,-1],
       "LEFT":[-1,0],
       "RIGHT":[1,0]}

#Set inputs
UP = int(input())
DOWN = int(input())
LEFT = int(input())
RIGHT = int(input())
data = ["UP 5", "DOWN 3","LEFT 3","RIGHT 2"]

#Move robot on valid moves
for inp in data:
    parts=inp.split()
    
    mv=parts[0]
    val=parts[1]
    if mv in moves and val.isnumeric():
        pos[0] = pos[0]+ moves[mv][0]*int(val)
        pos[1] = pos[1]+ moves[mv][1]*int(val)

#get distance     
distance=(int(round((pos[0]**2 + pos[1]**2)**0.5)))
print(distance, "from [0,0] to",pos)


# In[ ]:




