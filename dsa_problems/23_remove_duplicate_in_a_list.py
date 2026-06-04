def remove_duplicates(lst):
    unique = []
    for x in lst:
        if (x not in unique):
            unique.append(x)
    
    return unique
print(remove_duplicates([1,1,2,3,5,10,2]))