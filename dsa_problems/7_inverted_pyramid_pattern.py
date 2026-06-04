def generate_inverted_pyramid(n):
    pyramid = []
    for i in range(n):
        row = ""
        for j in range(i):
            row += " "
        for j in range(2*(n-i)-1):
            row += "*"
        for j in range(i):
            row += " "
        pyramid.append(row)

    return pyramid
a=generate_inverted_pyramid(4)
print(a)