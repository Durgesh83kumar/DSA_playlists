"""
pseudocode:

start
    function generate_triangle(n)
    create empty list called triangle
    repeat n times (for each row)
        create empty string called row
        repeat i times (for each column)
            add "*" in row
        add row in triangle

    return triangle

end
"""
def generate_triangle(n):
    triangle = []
    for i in range(n):
        row = ""
        for j in range(i+1):
            row += "*"
        triangle.append(row)

    return triangle
print(generate_triangle(5))