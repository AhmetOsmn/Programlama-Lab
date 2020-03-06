# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:34:04 2020

@author: Ahmet
"""
"""
event = istediğim olay
space = olabilecek durumlar
prime = asal sayılar
"""
from sympy import FiniteSet

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
