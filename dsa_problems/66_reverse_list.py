def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    n = len(lst)
    start = 0
    end = n-1
    while(start<end):
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1
        
    return lst