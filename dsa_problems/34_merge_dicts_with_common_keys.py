def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    start = 0
    merge_dicts = {}
    
    for dic in dicts:
        for k,v in dic.items():
            if(k not in merge_dicts):
                merge_dicts[k] = v
            else:
                merge_dicts[k] = merge_dicts[k] + v
    return merge_dicts 

dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
print(merge_dicts_with_overlapping_keys(dicts))
