from sympy import Symbol,Limit
from sympy import pprint
from sympy import exp,sqrt,pi,Integral

t = Symbol('t')
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
x = Symbol('x')

St = 5*t**2 + 2*t + 8

St1 = St.subs({t:t1})
St1_delta = St.subs({t: t1 + delta_t})

f_limit = Limit((St1_delta - St1)/delta_t,delta_t,0).doit()
#print("{}  fonksiyonun limiti: {}".format(St,f_limit))
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
f_integral = Integral(p,(x,11,12)).doit().evalf()
print(f_integral)
