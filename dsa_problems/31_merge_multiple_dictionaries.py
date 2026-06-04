def merge_three_dictionaries(dict1,dict2,dict3):
    result = {}
    for k,v in dict1.items():
        result[k] = v
    for k2,v2 in dict2.items():
        result[k2] = v2
    for k2,v2 in dict3.items():
        result[k2] = v2

    return result  

a = merge_three_dictionaries({'a':1,'b':2,},{'d':3,'e':7,'j':4},{'apple':2})
print(a)