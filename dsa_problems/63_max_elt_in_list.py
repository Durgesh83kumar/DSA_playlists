def find_max_element(lst):
    largest = lst[0]
    for i in range(len(lst)):
        if(largest<lst[i]):
            largest = lst[i]
    return largest

print(find_max_element([6,5,12]))