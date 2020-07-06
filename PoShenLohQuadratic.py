#quadratic calculator

import math

print("quadratic equations are of the form ax^2 + bx + c")
a = eval(input("a: "))
b = eval(input("b: "))
c = eval(input("c: "))

u = 0
h = b/2

#(h-u)(h+u)=c
#h^2-u^2 = c
#u^2=h^2-c
#u=root(h^2-c)

u = math.sqrt(h**2 - c)

x1 = -1*(h-u)
x2 = -1*(h+u)


print("The roots for this equation are: ", x1," and ",x2)

#made with <3 by tixpro lol
