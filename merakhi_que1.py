numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]#(dn)
i=0
c=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        c+=1
        print(c,':',"count",':',numbers[i])
    i+=1
