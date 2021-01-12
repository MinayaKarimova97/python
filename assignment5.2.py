# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:21:27 2021

@author: minaya.karimova
"""

largest = None
smallest = None
list1 = list()
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        istr = int(num)
        list1.append(istr)
    except:
        istr = -1
        print("Invalid input")
    
    
    
    print(num)
    
for i in list1:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
print('Maximum is', largest)


for j in list1:
    if smallest is None:
        smallest = j
    elif j<smallest:
        smallest = j
   
print('Minimum is', smallest)
