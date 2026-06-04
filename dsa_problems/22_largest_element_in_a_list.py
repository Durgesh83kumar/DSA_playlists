def find_largest(numbers):
    largest = numbers[0]
    for x in numbers:
        if(largest<x):
            largest = x
        
    return largest
        
print(find_largest([1,-2,9,4,0]))