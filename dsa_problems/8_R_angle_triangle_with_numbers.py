"""
pseudocode:

start
    function generate_number_triangle(n)
        create empty list called triangle
        repeat i, n times (for each column)
            create empty string called row
            repeat j, i+1 times (for each column)
                add "i+1" in row
            add row in triangle

        return triangle

end
"""
def generate_number_triangle(n):
    triangle = []
    for i in range(n):
        row = ""
        for j in range(i+1):
            row += f"{i+1}"
        triangle.append(row)
    return triangle
a = generate_number_triangle(5)
print(a)