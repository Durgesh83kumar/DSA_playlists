""" 
Why Your Logic Works

Euclidean Algorithm rule:

gcd(a, b) = gcd(b, a % b)

"""

def gcd(n,m):
    while(m!=0):
            temp = m
            m = n%m
            n = temp
    return n

print(gcd(9,10))