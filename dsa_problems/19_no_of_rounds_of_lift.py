def calculate_lift_rounds(n,capacity):
    rounds = n//capacity
    a = n%capacity
    if(a!=0):
        return rounds+1
    else:
        return rounds
    
print(calculate_lift_rounds(12,4))