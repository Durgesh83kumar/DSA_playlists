def check_unique(lst):
    unique = []
    for x in lst:
        if(x not in unique):
            unique.append(x)
        else:
            return False
    return True

print(check_unique([1,2,3,4,4]))