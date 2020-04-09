"""
Konular:

1.Liste uzerinde arama
2.Arama yapma
3.Siralama
4.Binary serch
5.mean,median,mode,wighted,geometric mean
"""

import random
"""
#print(random.random())

s = random.randint(1,100)
print(s)
"""
def random_sayi(n = 10,min = -5,max = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

#print(random_sayi())
#print(random_sayi(5,-10,10)) #5 Tane sayi al,-10 -- 10 arasinda
#Histogram demek:Her bir sayidan kac tane var ?
#print(random_sayi(15,-5,5))

liste =  random_sayi(15,-4,4)
#print(liste)
liste.sort()
#print(liste)
def my_frequency_with_list_of_tuples(liste):
    my_frequency_list = [] #eger bos liste olusturmazsak .append fonksiyonunu kullanamayiz.

    for i in range(len(liste)):
        s = False #i elemani listede yok anlaminda

        for j in range(len(my_frequency_list)):
            if(liste[i] == my_frequency_list[j][0]):
                my_frequency_list[j][1] = my_frequency_list[j][1]+1
                s = True #i elemani listede varmis.Alttaki if'e girmeyecek.

        if(s ==False):
            my_frequency_list.append([liste[i],1])

    return my_frequency_list


def my_frequency_with_dict(liste):
    frequency_dict = dict()

    for item in liste:
        if(item in frequency_dict):
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

print(my_frequency_with_dict(liste))

print(my_frequency_with_list_of_tuples(liste))
"""
liste2 = []
for i in histogram(liste).items():
    #print(i)
    liste2.append(i)

#print(liste2)
print("********************************")
for i in liste2:
    print("\t",i)
print("********************************")
"""
