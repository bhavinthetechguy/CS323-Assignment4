#Bhavinkumar Patel
#Akashkumar Patel

import math
import numpy as np

limit = 2 ** (-52)
iteration = 10
givenx = 2

def g1(x):
    return ((x**2) + 2)/3
def gf1(x):
    return (2*x)/3
def g2(x):
    return (3*x-2)** 0.5
def gf2(x):
    return 0.5 * ((3*x - 2) ** -0.5) * 3
def g3(x):
    return 3 - (2/x)
def gf3(x):
    return 2.0 / (x ** 2)
def g4(x):
    return ((x**2) -2)/(2*x-3)
def gf4(x):
    return ((-2.0 * (x**2 -2))/((2.0 * x -3) ** 2)) + ((2.0*x)/(2.0*x-3))
for i in range(0,1):
    k =0
    x = 2.1
    
    error = abs(x - givenx)
    print "---------------g1(x)---------------------"
    print "K:" ,' ',"X:" ,' ',"Error"
    print k,' ',x,' ',error
    print " K      X          Error"
    while error > limit and k < 10:
        k = k+1
        x = g1(x)
        newError = abs(x - givenx)
        ratio = newError/error
        error = newError
        print '%2d %10f %10f' % (k,x,error)
    #rate  = (x)
    #print "rate:",rate
    #print "Approximate Convergence Rate:", gf1(rate)
    print "This Function diverges and will become Infintely eventually"
print "\n"
for i in range(0,1):
    k =0
    x = 2.1
    
    error = abs(x - givenx)
    print "---------------g2(x)---------------------"
    print "K:" ,' ',"X:" ,' ',"Error"
    print k,' ',x,' ',error
    print " K      X          Error"
    while error > limit and k < 43:
        k = k+1
        x = g2(x)
        newError = abs(x - givenx)
        ratio = newError/error
        error = newError
        print '%2d %10f %10f' % (k,x,error)
    rate = (x)
    #print "rate:", rate
    print "Approximate Convergence Rate:", gf2(rate)
print "\n"
for i in range(0,1):
    k =0
    x = 2.1
    error = abs(x - givenx)
    print "---------------g3(x)---------------------"
    print "K:" ,' ',"X:" ,' ',"Error"
    print k,' ',x,' ',error
    print " K      X          Error" 
    while error > limit and k < 18:
        k = k+1
        x = g3(x)
        newError = abs(x - givenx)
        ratio = newError/error
        error = newError
        print '%2d %10f %10f' % (k,x,error)
    rate  = (x)
    #print "rate:",rate
    print "Approximate Convergence Rate:", gf3(rate)
print "\n"
for i in range(0,1):
    k =0
    x = 2.1
    error = abs(x - givenx)
    print "---------------g4(x)---------------------"
    print "K:" ,' ',"X:" ,' ',"Error"
    print k,' ',x,' ',error
    print " K      X          Error" 
    while error > limit and k < iteration:
        k = k+1
        x = g4(x)
        newError = abs(x - givenx)
        ratio = newError/error
        error = newError
        print '%2d %10f %10f' % (k,x,error)
    rate  = (x)
    #print "rate:",rate
    print "Approximate Convergence Rate:", gf4(rate)
