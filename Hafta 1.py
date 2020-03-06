def power_i(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    m = 1
    for i in range(b):
        m *= a
    return m

def power_i_recursive(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        if b % 2 == 0:
            return power_i_recursive(a*a,b/2)
        return power_i_recursive(a*a,int(b/2))*a

def find_max_renge(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            #print(i,j)
            t = 0
            for k in range(i,j+1):
                t = t + arr[k]

            if t > max:
                max = t
                i_1,i_2 = i,j
    return max,i_1,i_2

def find_max_renge_2(arr):
    max = 0

    for i in range(len(arr)):
        t = 0

        for j in range(i,len(arr)):
            t = t + arr[j]
            if t > max:
                max = t
                i_1,i_2 = i,j

    return max,i_1,i_2
