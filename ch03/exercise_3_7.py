#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:23:54 2018

@author: joy
"""

# Shrinking Guest List

invite_list = ['john', 'buddha', 'krishna']

print("Inviting",invite_list[0].title(), "to dinner.")
print("Inviting",invite_list[1].title(), "to dinner.")
print("Inviting",invite_list[2].title(), "to dinner.")

print(invite_list[0].title(), "can't make it to dinner.")

invite_list.remove('john')

invite_list.insert(0, 'gandhi')

print("Inviting",invite_list[0].title(), "to dinner.")
print("Inviting",invite_list[1].title(), "to dinner.")
print("Inviting",invite_list[2].title(), "to dinner.")

"""
# Better still:

for invitee in invite_list:
    print("Inviting", invitee.title(), "to dinner.")    
"""

print("Just found a bigger table. More accomodation possible!")

invite_list.insert(0, 'benjamin franklin')

middle_of_list = len(invite_list)//2 
invite_list.insert(middle_of_list, 'theodore roosevelt')

invite_list.append('mother teresa')

for invitee in invite_list:
    print("Inviting", invitee.title(), "to dinner.")  
    
print("Can only invite two guests to dinner!") 

while (len(invite_list) > 2):
    removed_guest = invite_list.pop()
    print("I'm sorry I can't invite you to dinner,", removed_guest, ".")

for invitee in invite_list:
    print(invitee.title(), "you're still invited to dinner.")    


del invite_list[1]
del invite_list[0]
    
print("Here's the invite list finally:")
print(invite_list)
