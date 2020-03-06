def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_f_1(arr):
    maxS = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            t = 0
            for k in range(i,j+1):
                t = t + arr[k]
                if(t > maxS):
                    maxS = t
    return maxS

def my_f_2(arr):
    maxS = 0
    n = len(arr)
    for i in range(n):
        t = 0
        for j in range(i,n):
            t = t + arr[j]
            if(t > maxS):
                maxS = t
    return maxS

def my_f_3(arr):
    n = len(arr)
    if(n == 1):
        return arr[0]

    left_i = 0
    left_j = n//2

    right_i = n//2
    right_j = n

    left_sum = my_f_3(arr[left_i:left_j])
    right_sum = my_f_3(arr[right_i:right_j])

    temp_left_sum = 0
    t = 0

    for i in range(left_j-1,left_i-1,-1):
        t = t + arr[i]
        if(t > temp_left_sum):
            temp_left_sum = t

    t = 0
    temp_right_sum = 0

    for i in range(right_i,right_j):
        t = t + arr[i]
        if(t > temp_right_sum):
            temp_right_sum = t

    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(left_sum,right_sum,center_sum)


l1 = [20,2,5,6,8,4,9,11,7,6,8]

print(my_f_1(l1))
print(my_f_2(l1))
print(my_f_3(l1))

print('\n\n\n')


#insertion_sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n): #0. indeksi listenin en büyük elemanı olarak aldık.
        key = arr[i]     #key değişkeni temp görevinde kullanılır.
        j = i-1          #sıralı kısmın son indeksindeki elemanını tutmuş oluyoruz.
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key   #son veriyi doğru yere koymuş oluyoruz.

l1 = [3,10,2,6,5,9]

insertion_sort(l1)

for k in range(0,len(l1)):
    print(l1[k])

print('\n\n\n')


#shell_sort
def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while(gap > 0):
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j>=gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j = j-gap
            arr[j] = temp
        gap = gap // 2
    return arr


l2 = [15,2,55,33,15,20,147,85,6,1,5,8,9,122,5,4,3]

shell_sort(l2)

for k in range(0,len(l2)):
    print(l2[k])
