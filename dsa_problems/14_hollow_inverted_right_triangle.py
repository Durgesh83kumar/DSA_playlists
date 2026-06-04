def generate_hollow_inverted_right_angled_triangle(n):
    hollow = []
    for i in range(n):
        row = ""
        if(i==0):
            for j in range(n):
                row += "*"
        else:
            for j in range(n-i):
                if(j==0 or j==n-i-1):
                    row += "*"
                else:
                    row += " "

        hollow.append(row)

    return hollow
a = generate_hollow_inverted_right_angled_triangle(5)
print(a)