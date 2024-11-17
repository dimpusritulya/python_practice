n=int(input())
a=0
b=1
flag=0
for a in range(n):
    if flag==1:
        break
    for b in range(n):
        ans = a**2+b**2
        if (ans) == n:
            flag=1
            print("Magical number")
            break
if flag==0:
    print('Ordinary')
