#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:29:46 2023

@author: sindhujaarivukkarasu
"""

import module

print(module.func(4))

from module import x
print(x)

import module
print(module.x)

car1=module.car()
print(car1.add(4))
