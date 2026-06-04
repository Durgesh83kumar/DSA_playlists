'''note: Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
'''
"""
Important Concept (Very Useful for Interviews)

There are 2 ways to represent negative numbers in binary:

1️⃣ Sign-Magnitude (what you did)
-5 → -101

2️⃣ Two’s Complement (real computer binary)

Steps:

For 5:

5 = 00000101
1's complement = 11111010
+1 = 11111011

"""
def int_to_binary(n):
    if n == 0:
        return "0"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    bin = ""
    while(n > 0):
        num = n // 2
        if(2 * num != n):
            bin += "1"
        else:
            bin += "0"
        n = n // 2
    
    lst = list(bin)
    start = 0
    end = len(lst) - 1
    while(start < end):
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    bin = "".join(lst)
    return sign + bin

print(int_to_binary(16))
print(int_to_binary(-16))
print(int_to_binary(5))
print(int_to_binary(-5))
print(int_to_binary(0))
