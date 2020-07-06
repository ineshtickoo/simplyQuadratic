#quadratic calculator

import cmath
import math
from fractions import Fraction as frac

print("Quadratic Equations are of the form f(x) = ax^2 + bx + c")
print("Input the desired values of a, b and c for f(x) = 0")
a = eval(input("a: "))
b = eval(input("b: "))
c = eval(input("c: "))

#declaring the half-value of b
#restructuring the equation by dividing the other coefficients by the value of a
h = (b/a)/2 
usq = h**2 - c/a #u^2
#(h-u)(h+u)=c
#h^2-u^2 = c 
#u^2=h^2-c
#u=root(h^2-c)

#solved values of x for f(x)
if (h**2-c/a)<0:                #for unreal roots
    u = cmath.sqrt(usq)
    x1 = -1*(h-u)
    x2 = -1*(h+u)
else:                           #for real roots
    u = math.sqrt(usq)
    x1 = frac(-1*(h-u))
    x2 = frac(-1*(h+u))    


print("The roots for this equation are: ", x1," and ",x2)

#made with <3 by tixpro lol
