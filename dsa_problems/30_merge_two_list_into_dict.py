def merge_lists_to_dictionary(keys,values):
    sett = {}
    if(len(keys) != len(values)):
        return False
    else:
        for i in range(len(keys)):
            sett[keys[i]] = values[i]
            

    return sett
a = merge_lists_to_dictionary(['a','b','c','d'],[1,2,3,4])
print(a)
a = merge_lists_to_dictionary(['a','b','c'],[1,2,3,4])
print(a)
a = merge_lists_to_dictionary([5,8,9,10],[1,2,3,4])
print(a)
a = merge_lists_to_dictionary([1,2,3,4],[2])
print(a)