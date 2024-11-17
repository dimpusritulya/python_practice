l=[5,3,2,-9,0,5,-3]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("after sorting")
for i in l:
    print(i,end='')