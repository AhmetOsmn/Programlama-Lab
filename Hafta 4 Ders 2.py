#from sympy import solve,sin
#import sympy
#import math

theta = Symbol('theta') #theta sadece değişken ismi,fakat Symbol classındaki theta özel semboldür.

#math.sin(theta)
#print(sympy.sin(theta)+sympy.sin(theta))


u = Symbol('u')
t = Symbol('t')
g = Symbol('g')
theta = Symbol('theta')


#print(solve(u*sin(theta)-g*t,t)) #(fonksiyonum,değişkenim).Değişkene göre fonksiyonu 0 yapan değeri bulur.

x = Symbol('x')

l = Limit(1/x,x,S,dir = '-')  #1/x fonksiyonunun x değişkeni için sonsuzdaki(s) limitini hesaplar.
l.doit()
'''
from sympy import Symbol #sympy modülündeki symbol classı.
from sympy import Limit,S

t = Symbol('t')
st = 5 * t**2 + 2 * t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
st1 = st.subs({t:t1})
st1_delta = (st.subs({t:t1+delta_t}))
f_d = Limit(((st1_delta-st1)/delta_t),delta_t,0) #limit ifadesinin kullanımı
print(f_d.doit())
