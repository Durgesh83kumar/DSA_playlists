def binary_to_decimal(binary_str):
    
    Decimal = 0
    n = len(binary_str)
    for i in range(n):
        digit = int(binary_str[n-1-i])
        Decimal += digit*(2**i)

    return Decimal
binary_str = "011"
print(binary_to_decimal(binary_str))