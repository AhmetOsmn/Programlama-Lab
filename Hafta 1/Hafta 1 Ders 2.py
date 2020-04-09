def selection_sort(arr):
    n = len(arr)
    swaps,comparsion = 0,0
    for key in range(n-1):
        for i in range (key+1,n):
            comparsion = comparsion + 1
            if arr[i] < arr[key]:
                swaps = swaps + 1
                arr[i],arr[key] = arr[key],arr[i]

    return arr,comparsion,swaps

#list_1 = [2,55,1,3,35,88,4,55,6,7,22,11]
#print(selection_sort(list_1))

def bubble_sort(arr):
    n = len(arr)
    swaps,comparsion = 0,0
    for i in range(n):
        for j in range(0,n-i-1):
            comparsion = comparsion + 1
            if arr[j] < arr[j+1]:
                swaps = swaps + 1
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr,comparsion,swaps

list_2 = [2,55,1,3,35,88,4,55,6,7,22,11]
print(bubble_sort(list_2))
