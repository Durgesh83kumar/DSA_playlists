"""
pseudocode: 

start
    function generate_hollow_square(n)
        create empty list
        repeat n times (for each row)
            create empty string called row
            for firstrow and lastrow
                repeat n times (for each column)
                    add "*" in row
            for rest rows
                repeat n times (for each column)
                    for firstcolumn and lastcolumn
                        add "*" in row
                    for rest columns
                        add space in row
            add row in square

        return square

end
"""
def generate_hollow_square(n):
    square = []
    for i in range(n):
        row = ""
        if (i==0 or i==n-1):
            for j in range(n):
                row = row + "*"
        else:
            for j in range(n):
                if(j==0 or j==n-1):
                    row = row + "*"
                else:
                    row = row + " "
        square.append(row)
        
    return square
print(generate_hollow_square(5))