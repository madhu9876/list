binary_number = [1, 0, 0, 1, 1, 0, 1, 1]#doubt
b=0
i=-1
s=0
while i<len(binary_number):
    s+=binary_number[i]*2**b
    b+=1
print(s)