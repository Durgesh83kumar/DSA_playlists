"""
pseudocode:

start
    create funtion(n)
        create empty list called diamond
        for unper half(including middel row)
        repeat n times(for each row)
            create empty string called row
            repeat n-1-i times(for each column)
                add space in row
            repeat 2*i+1 times
                add "*" in row
            repeat n-1-i times
                add space in row
            add row in diamond

        for lower half
        repeate n-1 times (for each row)
            create empty string called row
            repeat i+1 times
                add space in row
            repeat 2*(n-1-i)-1 times
                add "*" in row
            repeat i+1 times
                add space in row
            add row in diamond

            return diamond

end
"""

def generate_diamond(n):
    diamond = []
    for i in range(n):
        row = ""
        for j in range(n-1-i):
            row += " "
        for j in range(2*i+1):
            row += "*"
        for j in range(n-1-i):
            row += " "
        diamond.append(row)
    for i in range(n-1):
        row = ""
        for j in range(i+1):
            row += " "
        for j in range(2*(n-1-i)-1):
            row += "*"
        for j in range(i+1):
            row += " " 
        diamond.append(row)


    return diamond
a = generate_diamond(3)
print(a)