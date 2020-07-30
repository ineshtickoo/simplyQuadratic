# simplyQuadratic
Implementation of the Po-Shen Loh method of calculating Quadratics, without usign the quadratic formula
(inspired by https://www.poshenloh.com/quadraticdetail/)

[![Watch Po-Shen Loh's video explaination of this formula!](http://img.youtube.com/vi/XKBX0r3J-9Y/0.jpg)](http://www.youtube.com/watch?v=XKBX0r3J-9Y "Examples: A Different Way to Solve Quadratic Equations")

# How it works
In a quadratic equation:
f(x) = ax^2 + bx + c = 0

also, 

f(x) = (x-m)(x-n) = 0
In the above statement, m + n = b and m * n = c

Now this is where you'll see change in the flow,

m * n = c
and, m + n = b

Now for every two numbers whose sum is b, their average is b/2 (e.g., 7, 4 => 7+4 = 11 => (7+4)/2 = 11/2 = b/2)

So, 
<br> m = u-a
<br> n = u+a 
where a is the average (b/2)

m * n = c
(u-a)(u+a) = c
u^2 - a^2 = c
u = sqrt(a^2 - c)

u-a, u+a are the roots of the equation.
