#Bhavinkumar Patel
#Akashkumar Patel


import math
import numpy as np


def f1(x):
    return x**3 - 2*x - 5

def f2(x):
    return (math.e ** -x) - x

def f3(x):
    return x * math.sin(x) - 1

def f4(x):
    return (x ** 3) - 3* (x ** 2) + 3*x -1

def rate2( f, x, tolerance, ite ):

    x1 = x + 8.0 * tolerance
    x0 = -6.5 + 4.0 * tolerance

    fx0 = f(x0 )

    k = 0

    while k <= ite and abs( x - x0 ) >= tolerance:
        x2, x1, x0, fx1 = ( x1, x0, x, fx0 )
        fx0 = f( x0 )
        x = x0 - fx0 * ( x0 - x1 ) / ( fx0 - fx1 )
        #print "%2d %18.11e %18.11e" % ( k, x, abs( x - x0 ) )
        k = k + 1

    rate = math.log( abs((x - x0) / (x0 - x1)) ) / \
           math.log( abs((x0 - x1) / (x1 - x2)) )

    return (x,rate )
def rate1( f, x, tolerance, ite ):

    x1 = x + 8.0 * tolerance
    x0 = 20.0 + 4.0 * tolerance

    fx0 = f(x0 )

    k = 0

    while k <= ite and abs( x - x0 ) >= tolerance:
        x2, x1, x0, fx1 = ( x1, x0, x, fx0 )
        fx0 = f( x0 )
        x = x0 - fx0 * ( x0 - x1 ) / ( fx0 - fx1 )
        #print "%2d %18.11e %18.11e" % ( k, x, abs( x - x0 ) )
        k = k + 1

    rate = math.log( abs((x - x0) / (x0 - x1)) ) / \
           math.log( abs((x0 - x1) / (x1 - x2)) )

    return (x,rate )

def rate( f, x, tolerance, ite ):

    x1 = x + 8.0 * tolerance
    x0 = 2.82 + 4.0 * tolerance

    fx0 = f(x0 )

    k = 0

    while k <= ite and abs( x - x0 ) >= tolerance:
        x2, x1, x0, fx1 = ( x1, x0, x, fx0 )
        fx0 = f( x0 )
        x = x0 - fx0 * ( x0 - x1 ) / ( fx0 - fx1 )
        #print "%2d %18.11e %18.11e" % ( k, x, abs( x - x0 ) )
        k = k + 1

    rate = math.log( abs((x - x0) / (x0 - x1)) ) / \
           math.log( abs((x0 - x1) / (x1 - x2)) )

    return (x,rate )


def Secant(f,x1,x2,tolerance,iteration):
    print " i     x1            x2         Solution      Tolerance"
    x5 = x1 + 8.0* tolerance
    x4 = x2 + 4.0 * tolerance
    for i in range(1,iteration):
        x6 = x5
        x5 = x4
        x4 = x1
        
        fx1 = f(x1)
        fx2 = f(x2)
        solX = x2 - f(x2) * ((x1 - x2)/(f(x1) - f(x2)))
        error = abs((solX -x2)/x2)
        print '%2d %13.10f %13.10f %13.10f %13.10f' % (i,x1,x2,solX,error)
        if error < tolerance:
            sol = solX
            break
        x1 = x2
        x2 = solX
        if i == iteration:
            print "No answer"
            break
    rate = math.log( abs((solX - x4) / (x4 - x5)) ) / \
           math.log( abs((x4 - x5) / (x5 - x6)) )
    #print "Rate:",rate
        
def Secant1(f,x1,x2,tolerance,iteration):
    #print " i   x1          x2        Solution  Tolerance"       
    for i in range(1,iteration):
        fx1 = f(x1)
        fx2 = f(x2)
        solX = x2 - f(x2) * ((x1 - x2)/(f(x1) - f(x2)))
        tole = abs((solX -x2)/x2)
        if abs((solX - x2)/x2) < tolerance:
            sol = solX
            return sol
        #print '%2d %10f %10f %10f %10f' % (i,x1,x2,solX,tole)
        x1 = x2
        x2 = solX
        if i == iteration:
            print "No answer"
            break

print "---------------------------Secant----------------------------"
print "\n"
print "--------  function a ---------"
print "------start values = [0.82,2.82,] with Tolerance limit = 0.0001 ----"
print "Root of function a:", Secant1(f1,0.82,2.82,0.0001,30)
Secant(f1,0.82,2.82,0.0001,30)
x, rate = rate( f1,0.82 ,1e-8,30 )
print "Estimated Convergence Rate = %5.2f" % rate

print "\n"

print "--------  function b ---------"
print "------start values = [18,20] with Tolerance limit = 0.0001 ----"
print "Root of function b:", Secant1(f2,18.0,20.0,0.0001,30)
Secant(f2,18.0,20.0,0.0001,30)
x1, rate1 = rate1( f2,18.0 ,1e-8,30 )
print "Estimated Convergence Rate = %5.2f" % rate1
print "\n"

print "--------  function c ---------"
print "------start values = [-9.5,-6.5] with Tolerance limit = 0.0001 ----"
print "Root of function c:", Secant1(f3,-9.5,-6.5,0.0001,30)
Secant(f3,-9.5,-6.5,0.0001,30)
x2, rate2 = rate2( f2,-9.5 ,1e-8,30 )
print "Estimated Convergence Rate = %5.2f" % rate2
print "\n"

print "--------  function d ---------"
print "------start values = [2,1] with Tolerance limit = 0.0001 ----"
print "Root of function d:", Secant1(f4,2.0,1.0,0.0001,100)
Secant(f4,2.0,1.0,0.0001,100)
inf = "inf"
print "Estimated Convergence Rate:", inf
