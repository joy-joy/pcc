#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:17:17 2018

@author: joy
"""
# Seeing the World

visit_list = ["Machu Picchu", "Phuket", "Bali", 
              "Grand Canyon", "Santorini", "Dubai",  
              "New York City", "Paris", "London", "Sydney"]

print("\nVisit List:")
print(visit_list)

print("\nSorted List:")
print(sorted(visit_list))

print("\nOriginal List still preserved:")
print(visit_list)

print("\nReverse List:")
print(sorted(visit_list, reverse=True))

# Using the reverse() method on original list:
visit_list.reverse()
print("\nOrder has changed in the Original List:")
print(visit_list)

# Using the reverse() method to revert back to the original list:
visit_list.reverse()
print("\nOrder back to that of the Original List:")
print(visit_list)

# Using the sort() method to sort it (permanent change):
visit_list.sort()
print('\nSorted List using "sort()":')
print(visit_list)

# Using the sort() method to reverse sort it:
visit_list.sort(reverse = True)
print('\nReverse Sorted List using "sort()":')
print(visit_list)
