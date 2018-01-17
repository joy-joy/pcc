#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:23:54 2018

@author: joy
"""

# Changing Guest List

invite_list = ['john', 'buddha', 'krishna']

print("Inviting",invite_list[0].title(), "to dinner.")
print("Inviting",invite_list[1].title(), "to dinner.")
print("Inviting",invite_list[2].title(), "to dinner.")

print(invite_list[0].title(), "can't make it to dinner.")

invite_list.reomove('john')

invite_list.insert(0, 'gandhi')

print("Inviting",invite_list[0].title(), "to dinner.")
print("Inviting",invite_list[1].title(), "to dinner.")
print("Inviting",invite_list[2].title(), "to dinner.")

"""
# Better still:

for invitee in invite_list:
    print("Inviting", invitee.title(), "to dinner.")    
"""