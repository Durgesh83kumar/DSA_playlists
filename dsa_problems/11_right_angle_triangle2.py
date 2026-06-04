"""
pseudocode:

start
    creat function(n)
        create empty list called right
        repeat n times (for each row)
            create empty string called row
            repeat n-1-i times (for each column)
                add space in row
            repeat i+1 times
                add "*" in row
            
            add row in right
        
        return right
end
"""

def generate_right_angled_triangle(n):
    right = []
    for i in range(n):
        row = ""
        for j in range(n-1-i):
            row += " "
        for j in range(i+1):
            row += "*"
        right.append(row)

    return right
a = generate_right_angled_triangle(5)
print(a)