#Bhavinkumar Patel
#Akashkumar Patel


import math
import numpy as np

def f1(x):
    return x**3 - 2*x - 5
def dfdx1(x):
    return 3 *(x**2) -2

def f2(x):
    return (math.e ** -x) - x
def dfdx2(x):
    return -1 * math.e**(-x) - 1

def f3(x):
    return x * math.sin(x) - 1
def dfdx3(x):
    return x *math.cos(x) + math.sin(x)

def f4(x):
    return (x ** 3) - 3* (x ** 2) + 3*x -1
def dfdx4(x):
    return 3* x**2 - 6 *x + 3


def newton(f,dfdx,x0,tolerance,iteration):
    print " i       x1         Solution    Tolerance(abs)"
    x7 = x0 + 1.0 * tolerance
    x6 = x0 + 1.0 * tolerance
    for i in range(1,iteration):
        x5 = x7
        x7 = x6
        x6 = x0        
        x1 = x0 - (float(f(x0))/float(dfdx(x0)))
        computedTolerance = abs((x1-x0)/x0)
        print '%2d %13.10f %13.10f %13.10f' % (i,x0,x1,computedTolerance)
        if abs((x1-x0)/x0) < tolerance:
            xs = x1

            break
        else:
            x0 = x1
    rate  = math.log( abs((x1 - x6) / (x6 - x7)) ) / \
            math.log( abs((x6 - x7) / (x7 - x5)) )
    print "Approximate Convergence Rate.:",rate

    
def newton1(f,dfdx,x0,tolerance,iteration):
    n=1
    '''
    x7 = x0 + 8.0 * tolerance
    x6 = x0 + 4.0 * tolerance
    for i in range(1,iteration):
        x5 = x7
        x7 = x6
        x6 = x0
        
        x1 = x0 - (float(f(x0))/float(dfdx(x0)))
        computedTolerance = abs((x1-x0)/x0)
        print '%2d %13.10f %13.10f %13.10f' % (i,x0,x1,computedTolerance)
        if abs((x1-x0)/x0) < tolerance:
            xs = x1
            break
        else:
            x0 = x1
    '''
    while n <= iteration:
        
        x1 = x0 - (float(f(x0))/float(dfdx(x0)))
        if abs((x1-x0)/x0) < tolerance:
            xs = x1
            return xs
        else:
            x0 = x1        


print "------------------------Newton----------------------------"
print "\n"
print "--------  function a ---------"
print "------- initial x = 2 with tolerance limit =0.0001--------"
print "Root of function a:", newton1(f1,dfdx1,2.0,0.0001,30)
newton(f1,dfdx1,2.0,0.0001,30)
print "\n"

print "--------  function b ---------"
print "------- initial x = 2 with tolerance limit =0.0001--------"
print "Root of function b:", newton1(f2,dfdx2,2.0,0.0001,30)
newton(f2,dfdx2,2.0,0.0001,30)
print "\n"

print "--------  function c ---------"
print "------- initial x = 1 with tolerance limit =0.0001--------"
print "Root of function c:", newton1(f3,dfdx3,1.0,0.0001,30)
newton(f3,dfdx3,1.0,0.0001,30)
print "\n"

print "--------  function d ---------"
print "------- initial x = 2 with tolerance limit =0.0001--------"
print "Root of function d:", newton1(f4,dfdx4,2.0,0.0001,30)
newton(f4,dfdx4,2.0,0.0001,30)

