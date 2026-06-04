def rotate_left(ARR,D):
    n_arr = []
    k = D%len(ARR)
    if(k==0):
        n_arr = ARR
    else:
        for i in range(k,len(ARR)):
            n_arr.append(ARR[i])
        for j in range(0,k):
            n_arr.append(ARR[j])

    return n_arr
ARR = [1, 2, 3, 4, 5]
print(rotate_left(ARR,10))