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
