"""
pseudocode:

start
    function pyramid_pattern(n)
        create empty list called pyramid
        repeat n times (for each row)
            create empty string called row
            repeat n-i-1 times (for starting space in each  column)
                add " " in row

            repeat 2*i+1 times (for no. of stars)
                add "*" in row
            repeat n-i-1 times (for spaces after stars)
                add " " in row
            add row in pyramid
        
        return triangle

end
"""
def pyramid_pattern(n):
    pyramid = []
    for i in range(n):
        row = ""
        for j in range(n-i-1):
            row += " "
        for j in range(2*i+1):
            row += "*"
        for j in range(n-i-1):
            row += " "    
        pyramid.append(row)
        
    return pyramid

print(pyramid_pattern(4))