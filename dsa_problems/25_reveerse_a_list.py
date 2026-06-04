# def reverse_list(lst):
    # 
    # return lst[::-1]   # using slicing, it iterate from last
# 
# print(reverse_list([1,2,34,4,5]))
"""
pseudocode:
start
    function reverse_list(lst)
        create empty list called rev
        repeat len(lst) times in reverse order
            add each element in rev
        return rev
end
"""
def reverse_list(lst):
    rev = []
    for x in range(len(lst)-1,-1,-1):

        rev.append(lst[x])

    return rev
print(reverse_list([1,3,5,22,8]))
