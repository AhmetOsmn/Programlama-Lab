#liste sirali ise binary searh yapaibliyoruz.
import random

def random_sayi(n = 10,min = -5,max = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

def my_frequency_with_dict(liste):
    frequency_dict = dict()

    for item in liste:
        if(item in frequency_dict):
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

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

def my_linear_search(my_list,item_search):
    found = (-1,-1) #default,eger listede yok ise
    n = len(my_list)

    for indis in range(n):
        if(my_list[indis] == item_search):
            found = (my_list[indis],indis)

    return found

def my_mean(my_list):
    s,t = 0,0
    for item in my_list:
        s += 1
        t +=item
    mean = t/s
    return mean

def my_binary_search(my_list,item_search):
    found = (-1,-1)
    low = 0
    high = len(my_list) - 1

    while (low <= high):
        mid = (low + high) // 2

        if(my_list[mid] == item_search):
            return my_list[mid],mid
        elif(my_list[mid] > item_search):
            high = mid - 1
        else:
            low = mid + 1

    return found

def my_bubble_sort(my_list):
    n = len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j] < my_list[j+1]):
                #print("swap islemi")
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def my_median(my_list):
    my_list_2 = my_bubble_sort(my_list)
    #print(my_list_2)
    n = len(my_list_2)
    if(n%2 == 1):
        middle = int(n/2)+1
        median = my_list_2[middle]
        #print(median)
    else:
        middle_1 = my_list_2[int(n/2)]
        middle_2 = my_list_2[int(n/2)+1]
        median = (middle_1 + middle_2) / 2
        #print(median)

    return median




my_list = random_sayi(15,-4,4)
print(my_list)
print(my_bubble_sort(my_list),"Bubble Sort")
print("-----------------------------------------------------------------------")
print(my_median(my_list),"Median")
print("-----------------------------------------------------------------------")
print(my_binary_search(my_list,-2),"Binary Serach")
print("------------------------------------------------------------------------------------------------")
print(my_mean(my_list),"Mean")
print("------------------------------------------------------------------------------------------------")
print(my_linear_search(my_list,2),"Linear Search")
print("------------------------------------------------------------------------------------------------")
