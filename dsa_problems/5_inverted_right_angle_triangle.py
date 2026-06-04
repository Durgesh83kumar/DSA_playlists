"""
pseudocode:

start
    function generate_inverted_triangle(n)
        create empty list called triangle
        repeat n times (for each row)
            create empty string called row
            repeat i times (for each column in decrease)
                add "*" in row
            add row in triangle
        
        return triangle

end
"""
def generate_inverted_triangle(n):
    triangle = []
    for i in range(n):
        row = ""
        for j in range(n-i):
            row += "*"
        triangle.append(row)
        
    return triangle

print(generate_inverted_triangle(5))