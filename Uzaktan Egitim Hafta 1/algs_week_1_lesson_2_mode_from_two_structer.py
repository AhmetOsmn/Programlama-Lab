#mode = bir listedeki en cok tekrar eden eleman.
import random

def random_sayi(n = 10,min = -5,max = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

def my_mode_with_list_of_tuples(my_hist1_t):
    frequency_max = -1 #tekrar sayisi 0 dan kucuk olamaz.
    mode = -1

    for item,frequency in my_hist1_t:
        print(item,frequency)
        if(frequency > frequency_max):
            frequency_max = frequency
            mode = item

    return "En cok edilen tekrar sayisi: {},En cok tekrar eden sayi(mode): {} ".format(frequency_max,mode)
def my_mode_with_dict(my_hist1_d):
    frequency_max = -1
    mode = -1
    for key in my_hist1_d.keys():
        #print(key,my_hist1_d[key])
        if(my_hist1_d[key] > frequency_max):
            frequency_max = my_hist1_d[key]
            mode = key
        return "En cok edilen tekrar sayisi: {},En cok tekrar eden sayi(mode): {} ".format(frequency_max,mode)


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

my_list1 = random_sayi(15,-2,2)
print(my_list1)
my_hist1_d = my_frequency_with_dict(my_list1)
my_hist1_t = my_frequency_with_list_of_tuples(my_list1)
print(my_hist1_d,my_hist1_t)
"""
#--------------------------------------------------------
#dict'teyken mode nasil bulunur:
frequency_max = -1
mode = -1
for key in my_hist1_d.keys():
    #print(key,my_hist1_d[key])
    if(my_hist1_d[key] > frequency_max):
        frequency_max = my_hist1_d[key]
        mode = key

print("En cok edilen tekrar sayisi: {},En cok tekrar eden sayi(mode): {} ".format(frequency_max,mode))
#--------------------------------------------------------

"""
"""
#--------------------------------------------------------
#tuple'dayken mode nasil bulunur:
frequency_max = -1 #tekrar sayisi 0 dan kucuk olamaz.
mode = -1
for item,frequency in my_hist1_t:
    print(item,frequency)
    if(frequency > frequency_max):
        frequency_max = frequency
        mode = item
print("En cok edilen tekrar sayisi: {},En cok tekrar eden sayi(mode): {} ".format(frequency_max,mode))
#--------------------------------------------------------
"""
print(my_mode_with_dict(my_hist1_d))
print(my_mode_with_list_of_tuples(my_hist1_t))
