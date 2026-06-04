"""
pseudocode:

start
    function generate_floyds_triangle(n)
        create empty list called floyds
        create counter num = 1
        repeat n time (for each row)
            create empty string called row
            repeat i+1 times (for each column)
                for last column
                    add "num" in row
                else for other column
                    add "num" and " " in row
                increase num by 1
            add row in floyds

        return floyds
"""
def generate_floyds_triangle(n):
    floyds = []
    num = 1
    for i in range(n):
        row = ""
        for j in range(i+1):
            if(j==i):
                row = row + str(num)
            else:
                row = row + str(num) + " "
            num = num + 1
        floyds.append(row)

    return floyds
a = generate_floyds_triangle(5)
print(a)