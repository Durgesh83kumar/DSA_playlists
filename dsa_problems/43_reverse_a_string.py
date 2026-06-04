# def reverse_string(s):
#     st = ""
#     for i in range(len(s)-1,-1,-1):
#         st += s[i] # this create everytime new string 
#     return st
# print(reverse_string("susssss"))# TC = O(n**2)


def reverse_string(s):
    lst = []
    for i in range(len(s)-1,-1,-1):
        lst.append(s[i])
    
    return "".join(lst)
print(reverse_string("kuf"))# TC = O(n)