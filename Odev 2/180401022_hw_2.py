import csv
import sys

def my_mean(my_list):
    s,t = 0,0
    for item in my_list:
        s += 1
        t += item

    return t/s


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
           median = my_list_2[middle-1]
           #print(median)
       else:
           middle_1 = int(n/2)-1
           middle_2 = middle_1+1
           median = (my_list_2[middle_1]+my_list_2[middle_2])/2
           #print(median)

       return median


def frekans_tuple(liste):
    aylar = []

    for i in range(len(liste)):
        s =False
        for j in range(len(aylar)):
            if(liste[i] == aylar[j][0]):
                aylar[j][1] = aylar[j][1]+1
                s = True
        if(s == False):
            aylar.append([liste[i],1])


    return aylar


with open(sys.argv[1]+"/input_hw_2.csv","r") as file:
    data = csv.reader(file)
    cikis_ay = []


    for i in data:
               #print(i[0].split(";"))
        j = i[0].split(";")
                #print(j)

        for k in j[3]:
            cikis = j[3].split("-")

        ay = cikis[1].split(" ")
        cikis_ay.append(ay[0])


            #aylarin_frekansi = frekans_dict(cikis_ay)
            #print(aylarin_frekansi)
    aylarin_frekansi = frekans_tuple(cikis_ay)
            #print(aylarin_frekansi)


    liste = []

    for i in range(len(aylarin_frekansi)):
        aylarin_frekansi[i][0] = int(aylarin_frekansi[i][0])

                #print(aylarin_frekansi)
    #print(type(aylarin_frekansi[0][0]))

    for i in range(len(aylarin_frekansi)):
        liste.append(aylarin_frekansi[i][1])


    #print(liste)
    liste2 = my_bubble_sort(liste)
    #print(liste2)
    print("Medyan ve Ortalama output klasorune yazildi...")
with open(sys.argv[2]+ "/180401022_hw_2_output.txt","w") as file:
    median = my_median(liste2)
    file.write("Medyan: {}\n".format(median))
    file.write("Ortalama: {}\n".format(my_mean(liste2)))
