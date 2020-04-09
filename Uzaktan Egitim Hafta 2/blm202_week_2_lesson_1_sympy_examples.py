from sympy import Symbol
from sympy import factor,expand
from sympy import pprint

x = Symbol('x')
y = Symbol('y')

###############################################################################

y = 1
y = y + 1
print(y) #--> 2

x = Symbol('x')
x = x + 1
print(x) #--> x + 1

###############################################################################

x = Symbol('x')
y = Symbol('y')

p = x * (x + x) #--> 2*x**2
print(p)

###############################################################################

x = Symbol('x')
y = Symbol('y')

p = (x + 2)*(x + 3)
print(p) #--> (x + 2)*(x + 3)

###############################################################################

expr = x**2 - y**2
factors = factor(expr)
#factor() fonksiyonu verilen ifadeyi carpanlarina ayirir.
#print(factors)

expands = expand(factors)
#expand() fonksiyonu carpanlara ayrilmis ifadenin acilimini  yazar
#print(expands)
print(factors,"->",expands) #--> (x - y)*(x + y) -> x**2 - y**2

###############################################################################

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
#print(expr)
factors = factor(expr)
print(factors) #--> (x + y)**3

                #           3
pprint(factors) #--> (x + y)

###############################################################################

series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i

print(series) #--> x**5/5 + x**4/4 + x**3/3 + x**2/2 + x

               #     5    4    3    2
               #    x    x    x    x
pprint(series) #--> ── + ── + ── + ── + x
               #    5    4    3    2

###############################################################################

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
print(res) #--> 9
res2 = expr.subs({x:1-y}) #x'i yok et.
print(res2) #--> y**2 + 2*y*(1 - y) + (1 - y)**2

###############################################################################

series = x
n = 5
x_value = 5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print(series_value) #--> 10085/12
