# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:54:23 2021

@author: minaya.karimova


10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

d = dict()
d['csev'] = 2
d['cwen'] = 4
for k,v in d.items():
    print(k,v)
    
 
print('----------------')
tups = d.items()
print(tups)


c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
count = 0
lst1 = list()
lst2 = list()

for line in handle:
    if line.startswith('From '):
        lst1 = line.split()
       # print(lst1[5])
        lst2 = lst1[5].split(':')
       # print(lst2[0])
        d[lst2[0]] = d.get(lst2[0],0) +1
       # print(d)

for k,v in sorted(d.items()):
    print(k,v)
        
