#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:38:45 2018

@author: joy
"""
# Every function

countries = ['USA', 'UK', 'USSR', 'Brazil', 'India', 'Bangladesh', 
             'Pakistan', 'Mexico', 'Saudi Arabia', 'Australia']

print("\nHere's our initial list of countries:\n", countries)

# .append() - Adding an element/item:
countries.append('Peru')
print('\nList of countries with "Peru" added using ".append()":\n', countries)

# .insert() - Inserting an element/item:
print('\nCountry being deleted:', countries[-1])
del countries[-1]
print('List now with the country deleted\n', countries)

# .pop() - removing an element/item:
popped_country = countries.pop()
print("\nPopped country:", popped_country)    
print('List now with the country popped:\n', countries)

# popping by index
popped_country = countries.pop(-1)
print("\nPopped country:", popped_country)    
print('List now with the country popped:\n', countries)

# .remove() - removing an element/item by value:
print('\nRemoving country: "USSR"')
countries.remove('USSR')    
print('List now with the country removed:\n', countries)

# .reverse() - reversing order of the list:
countries.reverse()
print("\nReverse order now:\n", countries)
countries.reverse()
print("\nRevert back:\n", countries)
    

# .sorted() - Returns a sorted list, keeping original list unchanged
print('\nList sorted using "sorted()":\n', sorted(countries))    
print("\nHere's the original list unchanged:\n", countries)

# .sorted() - with parameter, reverse=True 
print('\nList reverse-sorted using "sorted()":\n',
      sorted(countries, reverse=True))    
print("\nHere's the original list unchanged:\n", countries)

# .sort() - Permanently sorting a list
countries.sort()
print("\nList permanently sorted:\n", countries)

# .sort() - Permanent reverse sort
countries.sort(reverse=True)
print("\nList permanently reverse-sorted:\n", countries) 

# len() function to find length of the list:
print("\nSize of the list (i.e. number of countries):", 
      len(countries))  

# modifying an element in the list (i.e. changing a country)
countries[0] = 'China'
print("How the list looks with the first country changed "
      + "to 'China'\n", countries)