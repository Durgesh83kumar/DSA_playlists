# # ........................with using the "in" keyword..................

# def is_subset(lst1, lst2):
#     # Your code goes here
#     for x in lst1:
#         if(x not in lst2):
#             return False
#     return True
                
# lst1 = [1, 2, 6] 
# lst2 = [1, 2, 3, 4, 5]
# print(is_subset(lst1,lst2))


# ........................without using the in keyword...................
def is_subset(lst1,lst2):
    for i in range(len(lst1)):
        found = False

        for j in range(len(lst2)):
            if(lst1[i]==lst2[j]):
                found = True
                break
        
        if(found == False):
            return False
    
    return True

lst1 = [1, 2, 3] 
lst2 = [1, 2, 3, 4, 5]
print(is_subset(lst1,lst2))