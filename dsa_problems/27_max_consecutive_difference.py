# def max_consecutive_difference(lst):
#     max_diff = []
#     if(len(lst)==0 or len(lst)==1):
#         maxx = 0
#     else:
#         for i in range(len(lst)-1):
#             if(lst[i]>lst[i+1]):
#                 max_diff.append(lst[i]-lst[i+1])
#             else:
#                 max_diff.append(lst[i+1]-lst[i])

#         maxx = max_diff[0]
#         for j in range(len(max_diff)-1):
#             if(max_diff[j]>max_diff[j+1]):
#                 maxx = max_diff[j]
#             else:
#                 maxx = max_diff[j+1]

#     return maxx
# print(max_consecutive_difference([1]))


def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(len(lst)-1):
        if(abs(lst[i]-lst[i+1])>max_diff):
            max_diff = abs(lst[i]-lst[i+1])

    return max_diff
print(max_consecutive_difference([1,2,-5]))