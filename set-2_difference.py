list1 = [1,2,3,4,5,6]#dn
list2 = [2,3,1,0,6,7]
i=0
list=[]
while i<len(list1):
    if list1[i] not in list2:
        list.append(list1[i])
    i+=1
print(list)