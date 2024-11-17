length=int(input())
l=list(map(int,input().split()))
j=2
flag2=0
for i in range(2,len(l)):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(l[i],end=' ')
        flag2=1

if flag2==0:
    print(-1)
    