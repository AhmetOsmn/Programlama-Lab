from sympy import exp,sqrt,pi,Integral
from sympy import Symbol

x = Symbol('x')

p = exp(-(x - 10)**2/2)/sqrt(2*pi)
f_integral = Integral(p,(x,11,12)).doit().evalf()
print(f_integral)
