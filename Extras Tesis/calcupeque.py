#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 13:02:40 2020

@author: kevinrojas
"""


import cmath
import numpy as np
import matplotlib.pyplot as plt



dom = np.linspace(0,1,1000)

Sol1 = []
Sol2 = []

for i in dom:
    Ra = i
    Rb = 1 - i

    a = 1
    b = ((1 + 5 * Rb)/(Rb - Ra)) - 100
    c = - (5 *Ra)/ (Rb - Ra)

    d = (b**2) - (4*a*c)

# find two solutions
    sol1 = (-b+cmath.sqrt(d))/(2*a)
    sol2 = (-b-cmath.sqrt(d))/(2*a)

    Sol1.append(sol1)
    Sol2.append(sol2)
    
fig1 = plt.figure(figsize=(10,10))
ax1 = fig1.add_subplot(111)
ax1.plot(dom, Sol1,"b-", label = "Solution 1")
ax1.plot(dom, Sol2,"b-", color ="black", label = "Solution 2")
ax1.axis(ymin=-300,ymax= 300)
ax1.set_xlabel('Proportion of rA')
ax1.set_ylabel("Value of solution")
ax1.set_title("Proportion-dependent Solutions")
ax1.legend()
plt.show()

fig1.savefig("Proportion-dependent-solution")    

  

