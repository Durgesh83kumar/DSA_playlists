def merge_two_sorted_lists(lst1,lst2):
    merged = []
    i = 0
    j = 0
    while(i<len(lst1) and j<len(lst2)):
        if(lst1[i]<lst2[j]):
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    while(i<len(lst1)):
        merged.append(lst1[i])
        i += 1
    while(j<len(lst2)):
        merged.append(lst2[j])
        j += 1

    return merged
a = merge_two_sorted_lists([1,2,3,4,5],[2,4,7,10])
print(a)