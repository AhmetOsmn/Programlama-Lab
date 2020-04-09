"""
Gauss mu-sigma formulu
"""
###############################################################################
import sympy as sy
from sympy import Symbol #degiskenleri sembol olarak kullanmamizi saglar.
from sympy import pprint #Ciktilarimizi gunluk hayatta kullandigimiz halde verir.
import sympy as sym #kutuphane
import sympy.plotting  as syp
import matplotlib.pyplot as plt #grafik cizmemizi sagliyor.
#%matplotlib inline #kodumuzu notbook veya browser'da yazarken grafigi cizmek icin ayri bir pencere acmamizi saglar.
###############################################################################

x = Symbol('x')
mu = Symbol('mu')
sigma = Symbol('sigma')

print(2*sym.pi*sigma) #--> 2*pi*sigma
pprint(2*sym.pi*sigma) #--> 2⋅π⋅σ

###############################################################################

print(sym.sqrt(2*sym.pi*sigma**2)) #--> sqrt(2)*sqrt(pi)*sqrt(sigma**2)

                                    #             ____
                                    #            ╱  2
pprint(sym.sqrt(2*sym.pi*sigma**2)) #--> √2⋅√π⋅╲╱  σ

###############################################################################

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sy.exp((-1*(x-mu)**2)/(2*sigma**2))

                #        √2
                #    ────────────
                #            ____
#pprint(part_1) #-->        ╱  2
                #    2⋅√π⋅╲╱  σ



                #             2
                #    -(-μ + x)
                #    ───────────
#pprint(part_2) #-->     2
                #     2⋅σ
                #    ℯ


my_gauss_function = part_1 * part_2

                           #               2
                           #      -(-μ + x)
                           #      ───────────
                           #             2
                           #          2⋅σ
                           #    √2⋅ ℯ
#pprint(my_gauss_function) #--> ───────────────
                           #             ____
                           #            ╱  2
                           #     2⋅√π⋅╲╱  σ

#1/√2 yazmamak için √2/2 olarak yazildi.

#grafik = syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution')
       #         (fonksion_adi.subs({mu:deger,sigma:deger}),(x,baslangic_degeri,bitis_degeri),title='grafik basligi')
#print(grafik)

###############################################################################

for value in range(-5,5):
    y = my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
                                                        #evalf() fonksiyonu:sqrt(2)*exp(-1/8)/(60*sqrt(pi)) yapisinin degerini hesapliyor.
    print("Value: ",value,"Y: ",y)

###############################################################################

x_values = []
y_values = []

for value in range(-5,5):
    y = my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print("Value: ",value,"Y: ",y)

plt.plot(x_values,y_values)
#plt.show()

###############################################################################

x_values = []
y_values = []

for value in range(-50,50):
    y = my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    #print("Value: ",value,"Y: ",y)

plt.plot(x_values,y_values)
#plt.show()

###############################################################################

x_values = []
y_values = []

for value in range(-50,50):
    y = my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    #print("Value: ",value,"Y: ",y)

plt.plot(x_values,y_values)
#plt.show() #eger grafigi alamazsak bu fonksiyonu kullaniyoruz.
