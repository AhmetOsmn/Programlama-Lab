
"""
event = istediğim olay
space = olabilecek durumlar
prime = asal sayılar
"""
from sympy import FiniteSet
from fractions import Fraction

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)

if t == s:
    print("True")
else:
    print("False")

print(t.union(s))
print(t.intersect(s))
print(t**2) 

def probability(space,event): #Olabilirlik
    return len(event)/len(space)

def check_prime(numb): #Asallık kontrolü
    if numb != 1:
        for factor in range (2,numb):
            if numb % factor == 0:
                return False
    
    else:
        return False
    
    return True


space = FiniteSet(*range(1,21)) # * işareti 1-20 arasındaki sayıları ',' ile birleştirerek küme yapısına sokar.
primes = [] # Eğer boş olmasaydı .append fonksiyonu çalışmaz.

for num in space:
    if  check_prime(num):
        primes.append(num)
    
event = FiniteSet(*primes)
p = probability(space,event)
print(p)
    
