from sympy import FiniteSet
from fractions import Fraction

def my_histogram(arr):
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    return my_dict

def lookup(dictt,value):
    try:
        for k in dictt:
            if dictt[k] == value:
                return k

    except:
        print("Value not found")

#exlist = [2,3,4,5,1,4,3,5,5]
#print(lookup(my_histogram(exlist),3)) #histogramda 3 defa kullanılan degeri yazdırır: 5

known = {0:0,1:1}

def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n] = result
        return result
"""
klasik yol:
    if n < 2:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
"""
"""
FiniteSet metodunu sonlu küme oluşturmak için kullanıyoruz.
Fraction metodunu kesirli sayı elde etmek için kullanıyoruz.

FiniteSet(0,1,3,Fraction(1,5)) = {0,1,1/5,3}
"""
s = FiniteSet(1,1.5,Fraction(1,5),1,1.5,7,42)
t = FiniteSet(Fraction(1,5),1,5,1,1,91,87)

for member in s:
    print(member)

if s == t:
    print("True")
else:
    print("False")

#print(s.union(t)) # t birleşim s kümesi
#print(s.intersect(t)) # t kesişim s kümsesi
#print(set(s ** 2)) # s ** 2 kartezyen çarpımı dır.set() fonksiyonu içinde kullanarak çarpımın elemanlarını görüyoruz.
