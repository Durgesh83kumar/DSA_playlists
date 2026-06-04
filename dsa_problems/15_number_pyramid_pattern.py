def generate_number_pyramid(n):
    pyramid = []
    for i in range(n):
        row = ''
        for j in range(n-i-1):
            row += ' '
        for j in range(i+1):
            if(j==0):
                row += str(1)
            else:
                 row += ' ' + str(j+1)
        for j in range(n-i-1):
            row += ' '


        pyramid.append(row)
        
    return pyramid

a = generate_number_pyramid(4)
print(a)