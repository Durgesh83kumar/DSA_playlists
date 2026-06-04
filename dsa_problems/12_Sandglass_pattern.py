"""
pseudocode:

start
    create function(n)
        create empty list called sand
        # for upper half(including smallest width)
        repeat n times 
            create empty string called row
            repeat i times
                add space in row
            repeat 2(n-i)-1 times
                add "*" in row
            repeat i times 
                add space in row
            add row in sand
        # for lower half
        repeat n-1 times
            create empty string called row
            repeat n-2-i times
                add space in row
            repeat 2i+3 times
                add "*" in row
            repeat n-2-i times
                add space in row
            add row in sand
        
        return sand
end

"""

def sandglass_pattern(n):
    sand = []
    for i in range(n):
        row = ""
        for j in range(i):
            row += " "
        for j in range(2*(n-i)-1):
            row += "*"
        for j in range(i):
            row += " "

        sand.append(row)
    for i in range(n-1):
        row = ""
        for  j in range(n-2-i):
            row += " "
        for j in range(2*i+3):
            row += "*"
        for j in range(n-2-i):
            row += " "
        sand.append(row)

    return sand
a = sandglass_pattern(4)
print(a)