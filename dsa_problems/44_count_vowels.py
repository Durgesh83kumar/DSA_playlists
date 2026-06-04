def count_vowels(s):
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


### pythonic way

def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)