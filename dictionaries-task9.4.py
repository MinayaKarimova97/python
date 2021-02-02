# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:59:03 2021

@author: minaya.karimova


jjj = {'mina' : 1, 'saadat' : 2, 'jala' : 3}
print(jjj)
ooo = {}
print(type(ooo))

ooo1 = []
print(type(ooo1))

names=['hgh', 'ghjhjhj', 'ddxx', 'ttdfd']
print(type(names))
"""

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the 
greatest number of mail messages. The program looks for 'From ' lines and takes the second 
word of those lines as the person who sent the mail. The program creates a Python dictionary 
that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop 
to find the most prolific committer.
"""


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
count = 0
lst1 = list()
bigcount = None
bigword = None

for line in handle:
    if line.startswith('From '):
        lst1 = line.split()
        d[lst1[1]] = d.get(lst1[1], 0) + 1
  
#print(d)

#en boyuk say

for k,v in d.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
        
print(bigword, bigcount)
    
