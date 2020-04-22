"""
180401022 Ahmet Osman Sezgin


Poisson Distribution
Poisson dagilimi, bir olayin bir zaman veya mekan araliginda kac kez meydana geldigini modellemek icin popülerdir.

llambda --> verilen ortalama.
x1,x2 --> İstenen aralik.


"""
from sympy import Symbol,factorial
from sympy import pprint
import matplotlib.pyplot as plt
import sympy as sy



def poisson_dist(l,x1,x2):
    llambda = Symbol('lambda') #llambda --> verilen ortalama.
    x = Symbol('x') #x --> İstenen aralik.


    my_function = ((llambda**x)*sy.exp(-1*llambda))/factorial(x)
    pprint(my_function)

    x_list = []
    y_list = []


    for value in range(x1,x2):
        y = my_function.subs({llambda:l,x:value}).evalf()
        y_list.append(y)
        x_list.append(value)
        print("x Value: {} -- P(x): {}".format(value,y))

    plt.plot(x_list,y_list)

poisson_dist(10,0,20)
