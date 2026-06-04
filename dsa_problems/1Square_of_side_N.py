"""
Pseudocode:
start
    function generate_square(n)
        create empty list called square
        repeat n times (for each row)
            create empty string called row
            repeat n times (for each column)
                add "*" to row
            add row to square
        return square

end function
"""

def generate_square(n):
    square = []
    for i in range(n):
        row = ""
        for j in range(n):
            row = row + "*"
        
        square.append(row)

    return square
print(generate_square(5))