n=int(input())
res=0
for i in range(len(str(n))):
    while n>1:
        a=n%10
        n=n//10
        res=res+a**2
if res==1:
    print('Happy Number')
else:
    print('Unhappy Number')