def sum_of_even_numbers(n):
    sum = 0
    for i in range(1,2*n+1):
        if(i%2==0):
            sum += i
    
    return sum

print(sum_of_even_numbers(100))