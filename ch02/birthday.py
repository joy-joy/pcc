#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:56:19 2018

@author: joy
"""

age = 23
message = "Happy " + age + "rd Birthday!"

print(message)

"""
message = "Happy " + age + "rd Birthday!"

TypeError: Can't convert 'int' object to str implicitly

"""

message = "Happy " + str(age) + "rd Birthday!"

print(message)
