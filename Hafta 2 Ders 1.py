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
