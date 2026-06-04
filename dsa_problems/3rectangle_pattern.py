"""
pseudocode:

start
    function generate_rectangle(n,m)
        create empty list called rect
        repeat n times (for each row)
            create empty string called row
            repeat m times (for each column)
                add "*" in row
            add row in rect
        return rect

end
"""
def generate_rectangle(n, m):
    rect = []
    for i in range(n):
        row = ""
        for j in range(m):
            row = row + "*"
        rect.append(row)

    return rect
print(generate_rectangle(2, 5))