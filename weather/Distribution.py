# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Alexander\.spyder2\.temp.py
"""
#
#from numpy import *
import matplotlib.pyplot as plt
import pylab

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump
    

#def f(t):
#    return t**2*exp(-t**2)
# 
#t = linspace(0, 3, 51)  # 51 
#y = f(t)
# 
##y = [1,2,3,8]
#plt.plot(y)
#plt.show()


R = 200
ro = 20
x = 0
y = 0
X = []
Y = []

    
for i in frange(x - 3*R, x + 3*R + ro, ro):
    for j in frange(y - 3*R, y + 3*R + ro, ro):
        if (2*R)**2 < i**2 + j**2 and i**2 + j**2 <= (3*R)**2:
            X.append(i)
            Y.append(j)
#xmin = -50.0
#xmax = 50.0
#plt.figure(num=None, figsize=(1, 1), dpi=10, facecolor='w', edgecolor='k')
            
pylab.xlim (-4*R, 4*R)
pylab.ylim (-4*R, 4*R)
plt.plot(X, Y, 'ro')
plt.show()