def sum_Of_elements(lst):
    sum = 0
    for i in range(0,len(lst)):
        sum += lst[i]

    return sum
print(sum_Of_elements([2,1,5,8,-7]))