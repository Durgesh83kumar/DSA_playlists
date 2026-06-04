"""
pseudocode:

start
    create function(n)
    create empty list called hollow
    repeat n times (for each row)


end

"""

def generate_hollow_right_angled_triangle(n):
    hollow = []
    for i in range(n):
        row = ""
        if(i<n-1):
            for j in range(n-1-i):
                print(" ")
            for j in range(i+1):
                if(j==0 or j==i):
                    row += "*"
                else:
                    row += " "
            hollow.append(row)

        else:
            for j in range(n):
                row += "*"
            hollow.append(row)

    # # if(i==n):
    # row = ""
    # for j in range(n):
    #     row += "*"
    # hollow.append(row)

    return hollow
a=generate_hollow_right_angled_triangle(4)
print(a)