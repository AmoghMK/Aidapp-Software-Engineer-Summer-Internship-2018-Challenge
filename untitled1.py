#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 02:54:45 2018

@author: amogh
"""

f=open("input.txt",'r')
s=f.read()
l=s.split('\n')

max_health=2000 #maximum health
max_injury=1000000 #maximum injury that can be sustained

n=int(l[0]) #number of monkeys to fight
l.pop(0) #list of n numbers, each specifying the damage that can be dealt by the monkey

for i in range(len(l)): #convert string to int
    l[i]=int(l[i]) 

maxcount=0 #variable used to store maximum count of monkeys that can be defeated
maxcountlist=[] #list to store index values from which maxcount was obtained

#algorithm to find the maximum number of monkeys that can be defeated
#loop starting from each position of list
for i in range(len(l)): 
    count=0
    health=0
    injury=0
    #increment count until health is lost or max injuries are sustained or end of list is reached
    while (health<max_health and injury<max_injury and (i+count)<len(l)):
        health=health+l[i+count]
        injury=injury*l[i+count]
        count=count+1
    #decrement count by 1 if health completely lost or max injuries sustained
    if (health>=max_health or injury>=max_injury):
        count=count-1
    #compare maxcount with new count and change maxcount if new count is greater
    if (count>maxcount):
        maxcount=count
        maxcountlist=[i]
    elif (count==maxcount):
        maxcountlist.append(i)

print(maxcount) #prints the maximum number of monkeys that can be defeated
print(len(maxcountlist)) #prints the number of times maxcount value was obtained
