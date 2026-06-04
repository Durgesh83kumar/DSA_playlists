def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    import string
    s = s.replace(" ","").lower()
    result = ""
    for char in s:
        if char not in string.punctuation:
            result += char
            
    for i in range(len(result)//2):
        if result[i] != result[len(result)-1-i]:
            return False
    return True
        