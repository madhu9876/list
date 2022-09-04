number = 30#dn
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
a=[]
while i<len(n):
    j=0
    b=[]
    while j<len(n):
        if n[i]+n[j]==30:
            b.append(n[i])
            b.append(n[j])
            a.append(b)
        j+=1
    i+=1
print(a)
